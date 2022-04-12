def person(name, surname, year, city, email, phone_number):
    result = f'Имя, фамилия: {name}, {surname}. Год рождения: {year}, город проживания: {city}, email: {email}, номер телефона: {phone_number}'

    return result

print(person('Yerlan', 'Mukhamejanov', 1995, 'Almaty', '1st.bianconeri@gmail.com', '87478960140'))