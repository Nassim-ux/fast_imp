from datetime import datetime
import itertools

class MailDetail:
    id_iter = itertools.count()
    def __init__(self, _gmail_id, _subject, _from, _to, _date, _attachments, _structured_attachments):
        
        mydate = _date
        mydate = mydate[4:]
        
        mydate_object = datetime.strptime(mydate, "%d%b%Y%H%M%S")
        
        self._id = next(MailDetail.id_iter)
        self._gmail_id = _gmail_id
        self._subject = _subject
        self._from  = _from
        self._to  = _to
        self._date  = mydate_object
        self._attachments = _attachments
        self._structured_attachments = _structured_attachments
    
    def displayMailDetail(self, full_name):
        
        if full_name:
            print("******************** MAIL ********************")
            print("       Id :  ", self._id)
            print("  Subject :  ", self._subject)
            print("     From :  ", self._from)
            print("       To :  ", self._to)
            print("     Date :  ", self._date)
            print(" GMAIL Id :  ", self._gmail_id)
            print("  L_Files :  ", self._structured_attachments)    
            print("**********************************************")
        else:
            print("******************** MAIL ********************")
            print("       Id :  ", self._id)
            print("  Subject :  ", self._subject)
            print("     From :  ", self._from)
            print("       To :  ", self._to)
            print("     Date :  ", self._date)
            print(" GMAIL Id :  ", self._gmail_id)
            print("    Files :  ", self._attachments)    
            print("**********************************************")
        
class Mail:
    id_iter = itertools.count()
    def __init__(self, _priority: int, _maildetail: MailDetail):
        self._id = next(Mail.id_iter)
        self._priority = _priority
        self._maildetail  = _maildetail
    
    def __repr__(self):
        return "{ id: " + str(self._id) + ", priority: " + str(self._priority) + ", subject: " + str(self._maildetail._subject) + ", date: " + str(self._maildetail._date) + ", gmail-id: " + str(self._maildetail._gmail_id) + ", from: " + str(self._maildetail._from) + " }"
    
    # def __gt__(self, other):
    #     if self._priority > other._priority:
    #         mydate = self._maildetail._date
    #         mydate = mydate[4:]
    #         othdate = other._maildetail._date
    #         othdate = othdate[4:]
            
    #         mydate_object = datetime.strptime(mydate, "%d%b%Y%H%M%S")
    #         othdate_object = datetime.strptime(othdate, "%d%b%Y%H%M%S")
            
    #         return mydate_object > othdate_object
    #     else:
    #         return False     

    # def __lt__(self, other):
    #     if self._priority < other._priority:
    #         mydate = self._maildetail._date
    #         mydate = mydate[4:]
    #         othdate = other._maildetail._date
    #         othdate = othdate[4:]
            
    #         mydate_object = datetime.strptime(mydate, "%d%b%Y%H%M%S")
    #         othdate_object = datetime.strptime(othdate, "%d%b%Y%H%M%S")
            
    #         return mydate_object < othdate_object
    #     else:
    #         return False    
    
    def displayMail(self):
        
        print("******************** MAIL ********************")
        print("       Id :  ", self._id)
        print(" Priority :  ", self._priority)
        print("  Subject :  ", self._maildetail._subject)
        print("     From :  ", self._maildetail._from) 
        print("     Date :  ", self._maildetail._date)
        print(" GMAIL Id :  ", self._maildetail._gmail_id)
        print("**********************************************")
    
    def removePriority(self):
        
        if self._priority < 2:
            self._priority += 1
    
    def addPriority(self):
        
        if self._priority > 0:
            self._priority -= 1
            
    
        