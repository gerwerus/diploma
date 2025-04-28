from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100, verbose_name="Отчество")
    birth_date = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"


class Account(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="accounts",
        verbose_name="Владелец",
    )
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Баланс"
    )
    update_date = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"Счет #{self.id} - {self.person}"

    class Meta:
        verbose_name = "Счет"
        verbose_name_plural = "Счета"


class InvestTest(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="invest_tests",
        verbose_name="Тестируемый",
    )
    name = models.CharField(max_length=200, verbose_name="Название")
    technical_name = models.CharField(
        max_length=100, unique=True, verbose_name="Техническое название"
    )

    def __str__(self):
        return f"{self.name} ({self.technical_name})"

    class Meta:
        verbose_name = "Инвестиционный тест"
        verbose_name_plural = "Инвестиционные тесты"
