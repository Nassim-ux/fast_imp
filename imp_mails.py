
import subprocess
import os
import base64
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

def finish_cmd(service, gmail_id):
    
	new_label_body = { 
		'removeLabelIds': [get_label(service, "inQueue")], 
		'addLabelIds': [get_label(service, "Processed"),get_label(service, "unNotified")] 
	}
	try:
		service.users().messages().modify(userId='me', id=gmail_id, body=new_label_body ).execute() 
	except:
		print("Error has ocurred.")
		return "fail"

	return "success"
                       
    
def print_mail(service, _mail, _printer, _folder):
	
	_color = ""
	_duplex = ""
	_delivery = ""
	_copies = ""

	match = re.findall( r'(?<=\[)(.*?)(?=\])', _mail._maildetail._subject)
	
	for option in match:
		if "couleur" in option.lower():
			_m = re.findall( r'\ ([a-zA-Z0-9]+)', option.lower())
			value = _m[0]
			if value == "oui":
				_color = "color"
			else:
				_color = "monochrome"
		elif "recto-verso" in option.lower():
			_m = re.findall( r'\ ([a-zA-Z0-9]+)', option.lower())
			value = _m[0]
			if value == "oui":
				_duplex = "duplex"
			else:
				_duplex = ""
		elif "livraison" in option.lower():
			_m = re.findall( r'\ ([a-zA-Z0-9]+)', option.lower())
			value = _m[0]
			if value == "oui":
				_delivery = "delivery"
			else:
				_delivery = ""
		elif "copies" in option.lower():
			_m = re.findall( r'\ ([a-zA-Z0-9]+)', option.lower())
			print(option.lower(),_m)
			_copies = _m[0]
	
	for item in _mail._maildetail._structured_attachments:
		_filename = os.path.join(_folder, item )
		try:
			subprocess.Popen(['SumatraPDF.exe', '-print-to', _printer, '-print-settings', f"{_color.lower()},{_copies}x,{_duplex}", _filename])
		except:
			print("Error printing: ", _filename, " to: ", _printer)
	
	response = finish_cmd(service, _mail._maildetail._gmail_id)

	return response
    
        

