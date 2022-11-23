from django.db import models

from CinemaWorld.CinemaWorld import settings


class Address(models.Model):
    zip_code = models.CharField(max_length=7)
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=32)
    house_flat_number = models.CharField(max_length=32)

    def __str__(self):
        return str(str(self.city) + " " + str(self.zip_code) + "\n" + str(self.street) + " " + str(self.house_flat_number))


class Cinema(models.Model):
    address_id = models.OneToOneField(Address, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    cinema_hall_qty = models.IntegerField()  #nie jestem pewien tego Integer Field

    def __str__(self):
        return self.name


class CinemaHall:
    hall_number = models.IntegerField()


class Seat(models.Model):
    cinema_hall_id = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    row_num = models.IntegerField()
    seat_num = models.IntegerField()

    def __str__(self):
        return str("Row: " + str(self.row_num) + "Num: " + str(self.seat_num))


class User(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    # login = models.CharField()
    # email = models.CharField()
    # name = models.CharField()
    # surname = models.CharField
    date_of_birth = models.DateField()

    # def __str__(self):
    #     return self.login

# TO BE FINISHED


class FilmCategory(models.Model):


    name = models.CharField(max_length=32)

    description = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Film(models.Model):
    GENERAL_AUDIENCE = 'G'
    PARENTAL_GUIDANCE_SUGGESTED = 'PG'
    PARENTS_STRONGLY_CAUTIONED = 'PG-13'
    RESTRICTED = 'R'
    ADULTS_ONLY = 'NC-17'

    Age_rating = (
        (GENERAL_AUDIENCE, "General Audiences"),
        (PARENTAL_GUIDANCE_SUGGESTED, "Parental Guidance Suggested"),
        (PARENTS_STRONGLY_CAUTIONED, "Parents Strongly Cautioned"),
        (RESTRICTED, "Restricted"),
        (ADULTS_ONLY, "Adults Only")
    )

    age_rating = models.CharField(max_length=32, choices=Age_rating, blank=False)
    film_category_id = models.ManyToManyField(FilmCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    duration = models.DurationField()
    director = models.CharField(max_length=64)
    release_date = models.DateField()
    ticket_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title


class FilmShowSeat(models.Model):
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
    is_seat_available = models.BooleanField()
    date_of_show = models.DateTimeField()

    #def __str__(self):


class Ticket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    film_show_seat_id = models.ManyToManyField(FilmShowSeat, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    #nie powinno byc jeszcze fk na jaki flm?


    # def get_list_of_seats_from_ticket(self):
    #     lista = FilmShowSeat.objects.
    #     list_of_seats = []
    #     for film in self.film_show_seat_id:
    #         list_of_seats.append(film.ticket_price)
    #
    #     return list_of_seats

# def __str__(self):  #ch wie w sumie co ma zwracac


