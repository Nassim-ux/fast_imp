
import base64
import os
from typing import List
import time
import re
from google_apis import create_service
from mails import Mail, MailDetail

class GmailException(Exception):
	"""gmail base exception class"""

class NoEmailFound(GmailException):
	"""no email found"""
    
def search_emails(service, query_string: str, label_ids: List=None):
	try:
		message_list_response = service.users().messages().list(
			userId='me',
			labelIds=label_ids,
			q=query_string
		).execute()
        
		message_items = message_list_response.get('messages')
		next_page_token = message_list_response.get('nextPageToken')
		
		while next_page_token:
			message_list_response = service.users().messages().list(
				userId='me',
				labelIds=label_ids,
				q=query_string,
				pageToken=next_page_token
			).execute()

			message_items.extend(message_list_response.get('messages'))
			next_page_token = message_list_response.get('nextPageToken')
		return message_items
	except Exception as e:
		return None
        # raise NoEmailFound('No emails returned')
        
def get_label(service, label_name):
    labels_list_response = service.users().labels().list(userId='me').execute()
    labels = labels_list_response.get('labels')
    label_id = ""
    for l in labels:
        if l.get("name") == label_name:
            label_id = l.get("id")
            break
    
    return label_id

def get_file_data(service, message_id, attachment_id):
	response = service.users().messages().attachments().get(
		userId='me',
		messageId=message_id,
		id=attachment_id
	).execute()

    
    
	file_data = base64.urlsafe_b64decode(response.get('data').encode('UTF-8'))
	return file_data

def get_message_detail(service, message_id, msg_format='metadata', metadata_headers: List=None):
	message_detail = service.users().messages().get(
		userId='me',
		id=message_id,
		format=msg_format,
		metadataHeaders=metadata_headers
	).execute()
	return message_detail

def fetch_mails(service, queue, save_location):
    
    query_string = 'is:unProcessed is:Confirmed has:attachment'
        
    email_messages = search_emails(service, query_string)
    
    if email_messages != None:
        
        for email_message in email_messages:
            messageDetail = get_message_detail(service, email_message['id'], msg_format='full', metadata_headers=['parts'])
            messageDetailPayload = messageDetail.get('payload')
            headers = messageDetailPayload['headers']
            
            for d in headers:
                if d['name'] == 'Subject':
                    subject = d['value']
                if d['name'] == 'From':
                    sender = d['value']
                if d['name'] == 'Date':
                    date = d['value']
                if d['name'] == 'Delivered-To':
                    deliveredTo = d['value']
            
            attachments = []
            structured_attachments = []
            
            if 'parts' in messageDetailPayload: 
                for msgPayload in messageDetailPayload['parts']: 
                    file_name = msgPayload['filename'] 
                    
                    
                    
                    body = msgPayload['body'] 
                    
                    if 'attachmentId' in body: 
                        attachment_id = body['attachmentId'] 
                        attachment_content = get_file_data(service, email_message['id'], attachment_id) 
                        
                        
                        match = re.search(r"<.+?>",sender)
                        sender = match.group()
                        sender = sender[1:-1]
                        
                        match = date[:25]
                        match = match.replace(' ', "")
                        date = match.replace(':', "")
                        
                        full_file_name = email_message['id'] + "_" + sender + "_" + date + "_" + file_name
                        
                        attachments.append(file_name)
                        structured_attachments.append(full_file_name)
                        
                        new_label_body = { 
                            'removeLabelIds': [get_label(service, "Confirmed"), get_label(service, "unProcessed")], 
                            'addLabelIds': [get_label(service, "inQueue")] 
                        } 
                        
                        service.users().messages().modify(userId='me', id=email_message['id'], body=new_label_body ).execute() 
                       
                        with open(os.path.join(save_location, full_file_name ), 'wb') as _f: 
                            _f.write(attachment_content) 
                            print(f'File {full_file_name} is saved at {save_location}') 
                        
                    time.sleep(0.5)
                
                maildetail = MailDetail(email_message['id'], subject, sender, deliveredTo, date, attachments, structured_attachments)
                maildetail.displayMailDetail(full_name= False)
                
                mail = Mail(1, maildetail)
                
                queue.append(mail)
                queue.sort(key= lambda x: (x._priority, x._maildetail._date))

        
def init_service():
    CLIENT_FILE = 'client-secret.json'
    API_NAME = 'gmail'
    API_VERSION = 'v1'
    SCOPES = ['https://mail.google.com/','https://www.googleapis.com/auth/gmail.modify','https://www.googleapis.com/auth/gmail.compose','https://www.googleapis.com/auth/gmail.send','https://www.googleapis.com/auth/gmail.settings.basic','https://www.googleapis.com/auth/gmail.readonly']
    
    service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)
        
    # create_label(service, "Processed")
    

    return service

def fetch(service, q, save_location):
    print('----------------------------------')
        
    print('Fetching...')
    fetch_mails(service, q, save_location)
    
    print('----------------------------------')
    
    if len(q) > 0:
        print('Queue :')
        i = 0
        for item in q:
            i += 1
            print("Item n° ", i)
            item.displayMail()
    else:
        print("Queue is empty.")
        
    return q



        
        
    