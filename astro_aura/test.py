import requests
import datetime
               
key='f095c27d00b647ce93c90328240810'
# location=requests.POST.get('name')                
Base_URL= f"http://api.weatherapi.com/v1//forecast.json?key={key}&q=delhi&days=11"  
response=requests.post(Base_URL)
data = response.json()
if response.status_code==200:
        try:  
           forecast = data.get('forecast',{}).get('forecastday',{})
           if not forecast:
                   print('data not avalible')
           else:       
               day_data=forecast[0] 
               my_dict={'time':[],'temp':[],'precip':[],'cloud':[],'humidity':[],'feels_like':[],'wind_mph':[],'pressure':[],'gust':[],'wind_dir':[],'icon':[]}             
               for x in range(0,24,3): 
                    hour_data=day_data['hour'][x]
                    datetime_obj=datetime.datetime.strptime(hour_data['time'], '%Y-%m-%d %H:%M')
                    time=datetime_obj.strftime('%H:%M')
                    temp=hour_data['temp_c']
                    precip=hour_data['precip_in']
                    cloud=hour_data['cloud']
                    humidity=hour_data['humidity']
                    feels_like=hour_data['feelslike_c']
                    wind_mph=hour_data['wind_mph']
                    pressure=hour_data['pressure_in']
                    gust=hour_data['gust_mph']
                    wind_dir=hour_data['wind_dir']
                    icon=day_data['hour'][x]['condition']['icon']
                    my_dict['time'].append(time)
                    my_dict['temp'].append(temp)
                    my_dict['precip'].append(precip)
                    my_dict['cloud'].append(cloud)
                    my_dict['humidity'].append(humidity)
                    my_dict['feels_like'].append(feels_like)
                    my_dict['wind_mph'].append(wind_mph)
                    my_dict['pressure'].append(pressure)
                    my_dict['gust'].append(gust)
                    my_dict['wind_dir'].append(wind_dir)
                    my_dict['icon'].append(icon)
        except ValueError:
                 print("Error decoding the JSON response")
else:
    print(f"Error: Received status code {response.status_code}")   

              
