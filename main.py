import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Sales Data.csv")
# print(df)

# 1. what we want to accomplish is to find out is what was the best month for sales and how much was earned in revenue that month

# 2. we want to find out what city has the highest number of sales

# 3. what product was often sold together

# 4. what product was sold the most and why do we think it was sold the most

def best_month():
    months_data = 'Month'
    extracted_months = df[months_data]
    #print(extracted_months)
    #print(df.dtypes)

    #this is grouping data together by month totals
    month_sum = df.groupby('Month').sum()
    #print(month_sum)

    #visual of our answer of finding out which month was the best for sales and earned revenue
    months_plot = [m for m, ss in df.groupby('Month')]
    plt.bar(months_plot, month_sum['Sales'])
    plt.title('Best Months For Sale & Revenue Generated')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.xticks(rotation='vertical')
    plt.yticks(month_sum['Sales'])

    df['Month']=df['Month'].replace([1,2,3,4,5,6,7,8,9,10,11,12], ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'])
    plt.show()
    #print(df)

#best_month()

def city_sales():
    #visual for finding out which city has the highest number of sales
    city_data = 'City'
    extracted_cities = df[city_data]
    #print(extracted_cities)
    city_sum = df.groupby('City').sum()
    #print(city_sum)

    city_plot = [m for m, ss in df.groupby('City')]
    plt.bar(city_plot, city_sum['Sales'])
    plt.title('Cities With the Most Sales')
    plt.xlabel('Cities')
    plt.ylabel('Sales')
    plt.xticks(rotation='vertical')   
    plt.yticks(city_sum['Sales'])
    plt.grid(axis='y', color='green')
    plt.show()

#city_sales()

def sold_together():
    # visual for what product was often sold together
    dupli = df[df['Order ID'].duplicated(keep=False)]
    #print(dupli)
    dupli['Together'] = df.groupby('Order ID')['Product'].transform(lambda x: ',' .join(x))
    #print(dupli)
    results = dupli.drop_duplicates(subset=['Order ID', 'Together'], keep="first")
    #print(results)
    results = results['Together'].value_counts().head(10)
    print(results)

    results.plot(kind = 'pie', autopct='%1.0f%%')
    plt.ylabel('')
    plt.title('Top 10 Items Most Sold Together')
    plt.show()

#sold_together()

def best_product():
    # visual for most sold product
    product_sum = df.groupby('Product').sum()
    #print(product_sum)

    product_plot = [m for m, ss in df.groupby('Product')]
    plt.figure(figsize= (15, 9))
    plt.plot(product_plot, product_sum['Quantity Ordered'])
    plt.title('Most Sold Product This Year')
    plt.xlabel('Product')
    plt.ylabel('Quantity Ordered')
    plt.xticks(rotation='vertical')   
    plt.yticks(product_sum['Quantity Ordered'])
    plt.grid()
    plt.annotate('Most Sold Product', xytext=('Apple Airpods Headphones', 31017), xy=('AAA Batteries (4-pack)', 31017), arrowprops={
        'facecolor':'green'
    })
    plt.annotate('Least Sold Product', xytext=('Bose SoundSport Headphones', 646), xy=('LG Dryer', 646), arrowprops={
        'facecolor':'green'
    })
    plt.show()

def main():
    best_month()
    city_sales()
    sold_together()
    best_product()

main()
