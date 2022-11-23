from django.db import models


class Address(models.Model):
    zip_code = models.CharField(max_length=7)
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    house_flat_number = models.CharField(max_length=32)

    def __str__(self):
        return str(str(self.city) + " " + str(self.zip_code) + "\n" + str(self.street) + " " + str(self.house_flat_number))


class Cinema(models.Model):
    address_id = models.ForeignKey(Address, on_delete=models.Cascade)
    name = models.CharField(max_length=32)
    cinema_hall_qty = models.IntegerField()  #nie jestem pewien tego Integer Field

    def __str__(self):
        return self.name


class Cinema_hall:
    hall_number = models.IntegerField()


class Seat(models.Model):
    cienma_hall_id = models.ForeignKey(Cinema_hall, on_delete=models.Cascade)
    row_num = models.IntegerField()
    seat_num = models.IntegerField()

    def __str__(self):
        return str("Row: " + str(self.row_num) + "Num: " + str(self.seat_num))


class User(models.Model):
    login = models.CharField()
    email = models.CharField()
    name = models.CharField()
    surname = models.CharField
    date_of_birth = models.DateField()

    def __str__(self):
        return self.login



class Ticket(models.Model): # nie wiem czy polaczenie ticket z film_show_seat jest prawidlowe bo maja swoje siebie jako fk nawzajem
    user_id = models.ForeignKey(User, on_delete=models.Cascade)
    #Film_show_seat_id = models.ForeignKey(Film_show_seat, on_delete=models.Cascade)
    price = models.IntegerField() #tu tez nie jestem pewien jaki field
    #nie powinno byc jeszcze fk na jaki flm?
    #def __str__(self):  #chuj wie w sumie co ma zwracac


class Film_category(models.Model):
    name = models.CharField(max_length=32)
    #age_rating = models.
    description = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Film(models.Model):
    film_category_id = models.ForeignKey(Film_category, on_delete=models.Cascade)
    title = models.CharField(max_length=128)
    duration = models.DurationField()
    director = models.CharField(max_length=64)
    release_date = models.DateField()
    ticket_price = models.IntegerField()  #to nie powinien byc fk do ticket?

    def __str__(self):
        return self.title


class Film_show_seat(models.Model):
    seat_id = models.ForeignKey(Seat, on_delete=models.Cascade)
    ticket_id = models.ForeignKey(Ticket, on_delete=models.Cascade)
    film_id = models.ForeignKey(Film, on_delete=models.Cascade)
    is_seat_avalaible = models.BooleanField()
    date_of_show = models.DateTimeField()

    #def __str__(self):
