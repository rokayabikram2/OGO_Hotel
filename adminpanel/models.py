from django.db import models
# from django.utils import timezone

class GlobalSettings(models.Model):
    SiteName = models.CharField(max_length=100)
    SiteContact = models.CharField(max_length=100)
    SiteEmail = models.EmailField()
    SiteAddress = models.CharField(max_length=500)
    Sitedescription = models.CharField(max_length=500,null=True)
    Sitefacebooklink = models.CharField(max_length=300)
    Sitelinkdinlink = models.CharField(max_length=300)
    Siteinstagramlink = models.CharField(max_length=300,null=True)
    logo = models.ImageField(upload_to="logo/",max_length=200, null=True, default=None)
    back_image = models.ImageField(upload_to="background/", null=True)
   

    def __str__(self):
        return self.SiteName


    

    


class Navigation(models.Model):
    PAGE_TYPE = (
        ('Home', 'Home'),('Normal', 'Normal'),('Group', 'Group'),('Home/Slider', 'Home/Slider'),('About', 'About'),
        ('Service', 'Service'),('Testimonial', 'Testimonial'),('Our Team', 'Our Team'),
        ('Service', 'Service'),('Contact', 'Contact'),('Booking','Booking'),
        
    )
        

    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft')
    )
    name = models.CharField(max_length=100, null=False)
    caption = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS, max_length=50)
    position = models.IntegerField()
    page_type = models.CharField(choices=PAGE_TYPE, null=True, blank=True, max_length=50)
    title = models.CharField(max_length=200)
    short_desc = models.TextField(null=True)
    desc = models.CharField(max_length=3000,null=True)
    bannerimage = models.ImageField(upload_to="bannerimage/",null=True)
    meta_title = models.CharField(max_length=100, null=True)
    meta_keyword = models.CharField(max_length=100, null=True)
    icon_image = models.TextField(null=True)
    image = models.ImageField(upload_to="image/", null=True)
    slider_image = models.ImageField(upload_to="sliderimage/", null=True)
    Parent = models.ForeignKey('self', related_name="childs", on_delete=models.CASCADE, null=True, blank=True)
    brochure = models.FileField(upload_to="brochure/",null=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    
    
    

    
class Booking(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    n_child= models.CharField(max_length=100,null=True)
    n_adult = models.CharField(max_length=100,null=True)
    checkIn = models.CharField(max_length=100,null=True)
    checkOut = models.CharField(max_length=100,null=True)
    rooms = models.CharField(max_length=100 ,null=True)
    n_rooms = models.CharField(max_length=50 ,null=True)
    message= models.TextField(null=True)

    def __str__(self):
        return self.name
    
    
class Rooms_detail(models.Model):
    name= models.CharField(max_length=200,null=True)
    image=models.ImageField(upload_to='rooms/',null=True)
    description = models.TextField(null=True)
    n_bed=models.CharField(max_length=20,null=True)
    n_bath=models.CharField(max_length=20,null=True)
    wifi=models.CharField(max_length=20,null=True)
    price=models.CharField(max_length=20,null=True)

    
    def __str__(self):
        return self.name
