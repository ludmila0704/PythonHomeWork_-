# однострочный генератор словаря
names = ['Борис', 'Маргарита', 'Руслан', 'Дариман']
premiums = [5000, 9500, 4000, 15000]  # ставка
rates = ['10.25%', '15.2%', '6.8%', '18.96%']  # премия в %

text_dict = {name: premium * float(rate[:-1]) for (name, premium, rate) in zip(names, premiums, rates)}

if __name__ == "__main__":
    print(text_dict)
