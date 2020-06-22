from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Raw_Ticks(models.Model):
    datetime = models.DateTimeField('tick time')
    instrument = models.CharField(max_length=10)
    price = models.FloatField(default=0)
    volume = models.IntegerField(default=0)

    def __str__(self):
        return str(self.datetime)+' '+self.instrument+' '+str(self.price)

    def get_first(self):
        return self.objects.first()

    def get_first10(self):
        list = []
        counter = 0
        for i in self.Raw_Ticks.objects.all():
            counter+=1
            if counter>10:
                break
            else:
                list.append(i)

        return list

