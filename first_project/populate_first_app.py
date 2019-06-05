import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

## Fake pop script
import random
from first_app.models import AccessRecord,webPage,Topic
from faker import Faker
fakegen = Faker()
topic = ['Search','Socil','MarketPlace','News','Games']
def add_topic():
    t= Topic.objects.get_or_create(top_name=random.choice(topic))[0]
    t.save()
    return t
def populate(N=5):

    for entry in range(N):
        #get the topic for the entry
        top = add_topic()
        # Create the fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        fake_add = fakegen.address()
        print(fake_add)
        #create new pweb page entry
        webpg = webPage.objects.get_or_create(topic = top,url=fake_url,name = fake_name)[0]

        # Create a fake access record for that web webPage
        acc_rec = AccessRecord.objects.get_or_create(name = webpg,date = fake_date)[0]

if __name__ == '__main__':
    print("populating database")
    populate(20)
    print("populating complete")
