class Movies:

    def __init__(self,title,rating,prod_budget,duration,release_date):

        self.title = title
        self.rating = None
        self.prod_budget = None
        self.duration = None
        self.release_date = None

        self.actors = []
        self.productors = []
        self.is3d = None
        self.marketing_budget = None

    def total_budget(self):
        
        if (self.prod_budget == None or self.marketing_budget == None):
            return None
        return self.prod_budget + self.marketing_budget    

class people:

    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname 
        self.id = id       

class pending() :
    import schedule
    import time

    def __init__(self):

        self.count = 0

        def job():
            print("I'm working...")
            self.count += 1

        self.schedule.every(10).seconds.do(job)
        #self.schedule.every().hour.do(job)
        #self.schedule.every().day.at("07:53").do(job)
        #self.schedule.every().monday.do(job)
        #self.schedule.every().tuesday.at("10:00").do(job)
        #self.schedule.every().minute.at(":17").do(job)
        # while True:
        #     self.schedule.run_pending()
        #     self.time.sleep(1) 

        while self.count < 5:
            self.schedule.run_pending()
            self.time.sleep(1)

        print('Go to close')
        exit()        
    
    




    


        
 
    