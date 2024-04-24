from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Countries",
                 ["Republic of India", "Democratic Republic of Russia", "People's Republic China", "Islamic Republic of Pakistan", "Kingdom of Saudi Arabia"])
table.add_column("Capitals", ["New Delhi", "Moscow", "Beijing", "Islamabad", "Riyadh"])

table.align = "l"

print(table)
