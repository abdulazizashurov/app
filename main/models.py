from django.db import models

class Subject(models.Model):
    subject = models.CharField('Fan Nomi',max_length=250)
    about = models.TextField('Fan haqida')
    price = models.IntegerField('Kurs narxi')
    num = models.IntegerField('Kurs Soni')

    def __str__(self):
        return self.subject


class Teacher(models.Model):
    name = models.CharField('Ism',max_length=250)
    img = models.ImageField(upload_to='media/')
    subject = models.ForeignKey(Subject,default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    facebook = models.CharField('Facebook',max_length=250)
    instagram = models.CharField('Instagram',max_length=250)
    telegram = models.CharField('Telegram',max_length=250)


    def __str__(self):
        return self.name


class New(models.Model):
    name = models.CharField('Yangilik Sarlavhasi:', max_length=300)
    about = models.TextField('Yangilik Haqida:')
    datetime = models.DateTimeField('Yangilik Qoyilgan Vaqti')




    def __str__(self):
        return self.name


class SocialNetwork(models.Model):
    image1 = models.ImageField('Birinchi Rasm:', upload_to='media/')
    image2 = models.ImageField('Birinchi Rasm:', upload_to='media/')
    image3 = models.ImageField('Birinchi Rasm:', upload_to='media/')
    facebook = models.CharField('Facebook', max_length=250)
    instagram = models.CharField('Instagram', max_length=250)
    telegram = models.CharField('Telegram', max_length=250)

    def __str__(self):
        return self.facebook


class Pupils(models.Model):
    first_name = models.CharField("O'quvchining ismi ",max_length=300)
    last_name = models.CharField("O'quvchining familyasi ",max_length=300)
    subject_name =models.CharField("Tanlangan Fan",max_length=300)
    phone = models.CharField("Telefon raqami:",max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name