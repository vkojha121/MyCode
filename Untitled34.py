#!/usr/bin/env python
# coding: utf-8

# In[13]:


def used_car_price(Year,Brand,Kmeter):
       if Year == 2021:
           if 10000 < Kmeter <= 15000:
               if Brand == 'Honda Amaze':
                   print('Rs 10,00,000 to 11,00,000')
               elif Brand == 'Hyundai Creta':
                   print('Rs 12,00,000 to 13,00,000')
               else:
                   print('Out if stok please visit after few months')
                   
           elif 15001 < Kmeter <= 25000:
               if Brand == 'Honda Amaze':
                   print('Rs 8,00,000 to 10,00,000')
               elif Brand == 'Hyundai Creta':
                   print('Rs 10,00,000 to 12,00,000')
               else:
                   print('Out if stok please visit after few months')
           else:
               print('No Stock')
               
       elif Year == 2020:
           if 10000 < Kmeter <= 15000:
               if Brand == 'Honda Amaze':
                   print('Rs 8,00,000 to 9,00,000')
               elif Brand == 'Hyundai Creta':
                   print('Rs 10,00,000 to 11,50,000')
               else:
                   print('Out if stok please visit after few months')
                   
           elif 15001 < Kmeter <= 25000:
               if Brand == 'Honda Amaze':
                   print('Rs 6,00,000 to 7,00,000')
               elif Brand == 'Hyundai Creta':
                   print('Rs 8,00,000 to 9,50,000')
               else:
                   print('No Stock')
                   
       else:
           print('We have only these stock right plese visit again')


# In[15]:


used_car_price(2021,'Hyundai Creta',11000)


# In[ ]:




