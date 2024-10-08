# Jyoti**shyam**itra is a tool for indian vedic astrology based software

## This tool takes the below mentioned birthdata and computes astrological data useful for a astrologer and astrology tool developer. You can use the data to further develop your own tool and anything else you want.

Birthdata Needed
- Name
- Gender
- DOB (Date of birth)
- POB (Place of birth - Longitude and lattitude and timezone (GMT) of the place)
- TOB (Time of birth in 24 hour format till seconds)



# The APIs provided by this module are explained below

## The APIs related to input for the module. 
### The API to provide input birthdata : `input_birthdata`
> input_birthdata to be used to provide input birthdata with below parameters.
>
> Input parameters all must be strings (Even numbers must be provided as strings)
>
> Parameters as below:
>> - **name** : its the name of the person whose astrological data you want to compute
>> - **gender** : This is gender of the person. *"male"* , *"female"* and *"others"* are the options
>> - **year** : this is the birth year of the person. it must be given in 4 digit format as a string ex: "1992"
>> - **month** : This is birth month of the person. you can either provide month number in string like "3" for March. Or else you can use the constants like *jyotishyamitra.September* Constants for All 12 months are provided. 
>> - **day** :This is the day part of date when the person was born. it also needs to be number provided as string like  "31" if the person is born on 31st of some month and year. 
>> - **hour** : This is hour part of birth time of the person. It is 24 hour format to be provided as string. ex: for 3 PM the value for hour will be "15" and for 3 AM it will be "3"
>> - **min** : This is minute part of birth time of the person. It is  to be provided as string. ex: for 3.25 the value for min will be "25".
>> - **sec** : This is seconds part of birth time of the person. This is not mandatory. if not provided it will take value of 0seconds. It is to be provided as string and only if you know exact second of birth time. ex: for 3.25.16 the value for min will be "16".
>> - **place** : This is the place name where the person was born. this also is a string. ex: "Honavar"
>> - **longitude** : This is the longitude of the birthplace. This is in Decimal degree format. For East the value will be positive number and for West it will be negative number. For example Honavar longitude is **74.4439° E** and so longitude value will be **"74.4439"**. Also if the Longitude of a place is **70° W 30'** then first convert 30 minutes to degrees which is 0.5 degrees. and since its west it will be negative. So longitude value will be **"-70.5"** in string format as you can see here. 
>> - **lattitude** : This is the lattitude of the birthplace. This is in Decimal degree format. The format is similar to longitude but here for North the value will be positive number and for South it will be negative number. For example Honavar lattitude is **14.2798° N** and so lattitude value will be **"14.2798"** in string format as you can see here. 
>> - **timezone** : This is the GMT tiezone value in decimal hour format. For example the timezone of Honavar is **GMT + 5 hr 30 min** and so the value of timezone will be **"+5.5"**. And for newyork the timezone is **GMT - 4 hr** and so the timezone value would be **"-4.0"** in string format as you can see here.
>
>This API returns the dictionary with all the provided input data till that point.

You can call this API to provide the input data in a single shot as shown below:
```python
#Providing birthdata of the person
inputdata = jyotishyamitra.input_birthdata(name="Shyam Bhat", gender="male", year="1991", month=jyotishyamitra.October, day="8", hour="14", min="47", sec="9", place="Honavar", longitude="+74.4439", lattitude="+14.2798", timezone="+5.5")

print(inputdata)
```

Alternatively you can provide the birthdata in multiple calls as shown below:
```python
#providing Name and Gender
inputdata = jyotishyamitra.input_birthdata(name="Shyam Bhat", gender="male")

#providing Date of birth details
inputdata = jyotishyamitra.input_birthdata(year="1991", month="10", day="8")

#Providing Place of birth details
inputdata = jyotishyamitra.input_birthdata(place="Honavar", longitude="+74.4439", lattitude="+14.2798", timezone="+5.5")

#Providing Time of birth details
inputdata = jyotishyamitra.input_birthdata(hour="14", min="47", sec="9")

print(inputdata)

```

---

### The API to clear input birthdata : `clear_birthdata`

This API is used to clear the birth data given previously. It returns the structure of birthdata which will be empty. 
It is highly recommended to call this API before providing fresh birth data using API `input_birthdata()`.

```python
#Clearing previlous input data to have a fresh start
inputdata = jyotishyamitra.clear_birthdata()

print(inputdata)

#Providing fresh birthdata of the person
inputdata = jyotishyamitra.input_birthdata(name="Shyam Bhat", gender="male", year="1991", month=jyotishyamitra.October, day="8", hour="14", min="47", sec="9", place="Honavar", longitude="+74.4439", lattitude="+14.2798", timezone="+5.5")

print(inputdata)

```
---

### The API to validate input birthdata : `validate_birthdata`
This API is used to validate all the birthdata provided using API `input_birthdata`. 
If any of birth data is not provided then this API shall provide that in string format. Or if any parameter format is wrong then also it returns that error in strong format.
If all the input birth datas are proper then this API returns "SUCCESS". Only after the data is validated then the input data can be used for further processing.

---

### The API to check if input birthdata is validated: `IsBirthdataValid`
This API is used to check if the input data is validated or not and if if its valid. Its return value is *boolean*
> Retrun value meanings
> - True: Input birthdata is validated and is Valid. 
>
> - False: Either the input birth data is not validated (API `validate_birthdata` is not called). If validated then birthdata is not valid.

---

### The API to get input birthdata after it is validated: `get_birthdata`
This API is used to get the input data as a dictionary once it is validated. This API returns the input birthdata if its validated successfully. If birthdata is not validated then this API returns `None`

---
---

## The APIs related to output for the module. 
### The API to provide output file destination and name : `set_output`
This API allows the user to provide a existing destination path and name of output json file in which the astrological data would be saved.
This API takes 2 parameters as input:
1. **path** : This should be the destination path where the output file has to be saved in the computer. The folder seperator must be "\\"(backslash). and at the end of folder there should not be any back-slash symbol. The this parameter given is invalid path then the API returns that error and the output path is not set.
2. **filename** : This is the name of the file without the extension. If this parameter is not provided then by default the name **astrodata** would be given to the file. 

If the output path and file name are set successfully then this function returns "SUCCESS". 
Example usage of this API is shown below:

```python
#To create D:\Project\jyotishyamitra\astroOutput.json.
#Note that Folder location D:\Project\jyotishyamitra must already exist in the system for this API to work. 
status = jyotishyamitra.set_output(path="D:\Project\jyotishyamitra", "astroOutput")

print(status)
```
---

### The API to get output json file full name with location : `get_output`
This API gives you full location of the generated json file with astrological data.
Always make sure that this APIn is called only after `set_output` is called to set the destination first. 
Below the example code to demonstrate the usage of the API is given

```python
 
status = jyotishyamitra.set_output(path="D:\Project\jyotishyamitra", "astroOutput")
if (status == "SUCCESS"):
    print(jyotishyamitra.get_output())
#This results in output : 'D:\Project\jyotishyamitra\astroOutput.json'

```

---
---

## The APIs related to astrological data generation 
### The API to generate Astrological data from birthdata given and save it in output file in json format `generate_astrologicalData`

This is the most important API of this module. This API takes valid birthdata which is returned by API `get_birthdata` after the input data is validated as input and computes the astrological data based on indian vedic astrology and siderial ayanamsha and nirayana method and stores all those computed astrological data either in json format in the file created in the location set by API `set_output` or in a dictionary depending on the input parameter **returnval**. 

This API takes 2 input parameters : 
- birthdata: This is the dictionary of all the provided birth data which can be fetched by calling the API `get_birthdata`. This is a *mandatory* input parameter for this API.
- returnval: This is a *optional* parameter. This specifies in which format the Astrological data has to be provided by this API. 
    -If the value is either not provided or mentioned as **"JSON_FILE_LOCATION"**, Then output will be put in a JSON file and the location of the file will be returned by this API. 
    -If the value is given as **"ASTRODATA_DICTIONARY"**, Then output will be put in a dictionary format and that dictionary will be returned by this API
    -If any other value is provided for this input parameter then it returns error saying **"Invalid parameter returnval"**


> **Note** : If input birth data is not provided properly and not validated successfully before calling this API then it returns **"INPUT_ERROR"** and doesnt compute any astrological data. Similarly if output path is not provided using API `set_output` before calling this API and in the API the return of JSON file expected, then it returns **"OUTPUTPATH_ERROR"** and doesnt compute any astrological data as well. 

> Below listed astrological data are computed by this module
> - User Details like name, rashi, nakshatra, vaara, tithi, karana, maasa etc along with birth details
> - Lagna chart components ascendant, planets and their sign, house, nakshatra, nakshatra lord, their friends, enemies etc
> - All 16 Varga chart details and vargottama 
> - functional and natural benefics and malefics in the chart
> - Different planetery balas like vimshopaka bala, Shadbala and their sub divisions
> - Strengths of houses - BhavaBalas and their sub divisions (Adhipathi bala, Digbala and drishti bala)
> - AshtakaVarga - Bhinna Ashtakavarga of all 7 planets from Sun to Saturn and Sarvashtaka varga
> - and many many more....
>
> To clearly understand all the various astrological data computed in detail refer to section of Astrological Datas.

---
---

# Order of API invocation to compute Astrological data of a person in a JSON file

Below Steps have to be followed in API invocation to get the Astrological data properly. 
1. Clear the past input data residue by calling `clear_birthdata`
2. Provide input birth data by calling `input_birthdata` in a single shot or multiple steps. Make sure all the input birth data is provided.
3. Validate the input data by calling `validate_birthdata`
4. Check if birthdata is valid using API `IsBirthdataValid` and if yes then get the **birthdata** by calling `get_birthdata`. This return value of API `get_birthdata` is important and store this birthdata dictionary in a variable which will be passed as input variable in next steps to compute astrological data. 
5. Provide the location and filename for output file where computed astrological data would be stored by invoking API `set_output`. Make sure this API returns `'SUCCESS'` to make sure the location provided is proper.
6. Invoke `generate_astrologicalData` with input parameter **birthdata** we had fetched in step 4 as input parameter to this api. The return value is the output json file with its location where the astrological data are generated. 
7. If you want to fetch the output file full name (path with name) then you can also get it by invoking `get_output` API. 
Hence the Astrological data is computed for given birth data in json file format. 

### Below code snippet demonstrates the steps provided above :

```python
import jyotishyamitra as jsm

#step 1 :clear past input data
jsm.clear_birthdata()

#Step 2: Providing input birth data - here multiple times the API input_birthdata are invoked but you can do it in single shot too.
#providing Name and Gender
inputdata = jsm.input_birthdata(name="Shyam Bhat", gender="male")

#providing Date of birth details
inputdata = jsm.input_birthdata(year="1991", month=jsm.October, day="8")

#Providing Place of birth details
inputdata = jsm.input_birthdata(place="Honavar", longitude="+74.4439", lattitude="+14.2798", timezone="+5.5")

#Providing Time of birth details
inputdata = jsm.input_birthdata(hour="14", min="47", sec="9")

#Step 3: Validate Birthdata
jsm.validate_birthdata()

#Step 4: If Birthdata is valid then get birthdata
if(jsm.IsBirthdataValid()):
    birthdata = jsm.get_birthdata()


#Step 5: Set the output folder and name of file to save generated astrological data
if("SUCCESS" == jsm.set_output(path="D:\OutFolder", filename="astroOutput")):
    #Step 6: Computing Astrological data
    jsm.generate_astrologicalData(birthdata)    #Compute the astrological data based on new set.
    print(f'The output is : {jsm.get_output()}')    #step 7: to get output file full name
else:
    print("Given folder path doesnt exist")
    

```
---
# Order of API invocation to compute Astrological data of a person in a dictionary

Below Steps have to be followed in API invocation to get the Astrological data properly. 
1. Clear the past input data residue by calling `clear_birthdata`
2. Provide input birth data by calling `input_birthdata` in a single shot or multiple steps. Make sure all the input birth data is provided.
3. Validate the input data by calling `validate_birthdata`
4. Check if birthdata is valid using API `IsBirthdataValid` and if yes then get the **birthdata** by calling `get_birthdata`. This return value of API `get_birthdata` is important and store this birthdata dictionary in a variable which will be passed as input variable in next steps to compute astrological data. 
5. Invoke `generate_astrologicalData` with input parameter **birthdata** we had fetched in step 4, and **returnval** value **"ASTRODATA_DICTIONARY"** as input parameters to this api. The return value is the dictionary where the astrological data are computed and updated. 

Hence the Astrological data is computed for given birth data in dictionary format using which yopu can process further as you wish. 

### Below code snippet demonstrates the steps provided above :

```python
import jyotishyamitra as jsm

#step 1 :clear past input data
jsm.clear_birthdata()

#Step 2: Providing input birth data - here multiple times the API input_birthdata are invoked but you can do it in single shot too.
#providing Name and Gender
inputdata = jsm.input_birthdata(name="Shyam Bhat", gender="male")

#providing Date of birth details
inputdata = jsm.input_birthdata(year="1991", month=jsm.October, day="8")

#Providing Place of birth details
inputdata = jsm.input_birthdata(place="Honavar", longitude="+74.4439", lattitude="+14.2798", timezone="+5.5")

#Providing Time of birth details
inputdata = jsm.input_birthdata(hour="14", min="47", sec="9")

#Step 3: Validate Birthdata
jsm.validate_birthdata()

#Step 4: If Birthdata is valid then get birthdata
if(jsm.IsBirthdataValid()):
    birthdata = jsm.get_birthdata()


#Step 5: Invoke the API generate_astrologicalData with retrunval desired to be dictionary and get astrological data in dictionary format.
astrodata = jsm.generate_astrologicalData(birthdata, returnval = "ASTRODATA_DICTIONARY")    print(astrodata)
    

```

---
---

# The Contents of Astrological Data stored in output JSON file:

The below image shows the various Astrological Data generated by this module:
![This image cant be displayed here. Sorry](readmefiles/astrojson_structure.png)

---

## The sections in Generated output JSON file

The JSON file has below main sections:
- **Main Lagna Chart Data**  (D1)
- **All 15 Divisional charts Data** (D2, D3, D4, D7, D9, D10, D12, D16, D20, D24, D27, D30, D40, D45, D45, D60)
- **Various strengths of Planets and houses** (Balas) 
- **Ashtakavarga** (Bhinna Ashtakavarga of 7 planets fron Sun to Saturn and Sarvashtakavarga)
- **Dashas** (Currently contains Vimshottari dasha - Mahasasha, Antarshashas and paryantardashas along with current running dashas when this module is executed This section and subsections are self explanatory and so pleae have a look.)
- **User Details** (Miscellaneous details of the person)

---

## The Subsection of each section is explained below:
### Divisional Chart Data:
This explains subsections of 16 divisions in ShodashaVarga (16 divisions given by maharshi Parashara). This contains below mentioned details. Here Dx will mean that this field is part of all Divisional charts. 
- **Dx -> name** : name of the division (Dx is corresponding Division) : *Lagna, navamsa, .... shashtiamsa etc.*
- **Dx -> symbol** : The symbol of the division : *D1, D2, D3, ... D60 (16 Divisions)*
- **Dx -> ascendant** : This contains astrological details related to 1st house of the divisional chart and its lord. 
- **Dx -> planets** : Contains the astrological data of all 9 planets in the divisional chart. The structure of each planet (Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn, Rahu, Ketu) is same and its astrological datas are explained after this section with the name *planet* 
- **Dx -> houses** : This contains 12 elements starting from index 0 to 11 containing astrological data of 12 houses in the divisional chart. In further section The content structure of each house is explained with the name *house*
- **Dx -> classifications** : This contains the 9 planets classified into various groups like *benefics* and *malefics* and *kendra planets*, *trikon planets* etc. The different classifications made are explained clearly below:
    - **Dx -> classifications -> (benefics/malefics/neutral)** : These are the functional benefic/malefic/neutral planet list depending on the lagna of the chart and houses they are given. 
    - **Dx -> classifications -> (natural benefics/natural malefics)** : These are the natural benefic/malefic planet list in the divisional chart depending on its natural tendency. Sun, Mars, Saturn, Rahu and Ketu are always natural malefics. Jupiter and Venus are always natural benefics. Moon is benefic if its in shukla paksha and malefic if in krishna paksha. Mercury is normally a natural benefic but turns natural malefic if conjoint with a natural malefic.
    - **Dx -> classifications -> (kendra/trikona/trik/upachaya)** : These grouping are based on planets house placements. Parashara has grould certain houses and tagged with auspicious or inauspicious houses. For example trikona is houses 1,5 and 9. So planets in these houses will be categorised under trikona classification. Similarly kendra houses are 1,4,7 and 10. Trik houses are bas houses which are 6,8 and 12. And finally upachaya houses which are 3,6,10 and 11. 
    - **Dx -> classifications -> (dharma/artha/kama/moksha)** : In a astrological chart the 12 houses are divided into 4 kinds of trikon namely dharma(houses : 1,5,9), artha(houses : 2,6,10), kama(houses : 3,7,11) and moksha(houses : 4,8,12). The planets list in each of these trikonas are enumerated in these classifications. 
- **Dy -> vargottamas** : This section is available for all divisional parts except for D1. A vargottama planet is one which is in same sign in the divisional chart as in D1 chart. A vargottama planet is equivalaent to exhalted planet in that divisional chart.

### Planetery and House Strength Data:
This explains the subsections under sthe section **Balas**. This includes strengths of houses which is bhavabala and planetery strengths which includes vimshopakabala, Shadbala and ishta-kashta balas 
- **Balas -> Vimshopaka** : This is planetery balas provided by parashara basedon their placements. Points out of 20 will be given to each of 9 planets with 20 being highest and 5 being lowest. Higher is the points, stronger and happier is the planet. These points are calculated based on if the planet is placed in own sign or friend sign or emnemy sign etc in multiple divisional charts. The weightage given for various divisional charts are also differs bsed on number of divisional charts considered. So 4 group of divisional charts are described by Parashara. Namely Shadvarga (6 Divisional charts), SaptaVarga (7 Divisional charts), DashaVarga (10 Divisional charts) and shodashavarga (16 Divisional charts). And in this output file all four groupwise calculations are made and vimshopaka bala of each of 9 planets are given under them. 
- **Balas -> Shadbala** : This is a major planetery strength metric provided by parashara for 7 planets from Sun to Saturn. As the name suggests it is sum of 6 different kinds of strengths (Shad means six and bala means strength). The shadbala is calculated and provided in unit of virupas for all subsections except for **Rupas** where shadbala is converted in unit of Rupas for all planets. (1 rupa = 60 virupas). So there are  six subsections of the Shadbala each for  6 sub-balas and 2 subsections for total. one in unit of rupas and one in virupas as shown below:
    - **Balas -> Shadbala -> Sthanabala** : This is the positional strength of planets. This further has sub categories as shown below:
        - **Balas -> Shadbala -> Sthanabala -> Uchhabala** : This section computes exhaltation strength of planets in the chart in virupas
        - **Balas -> Shadbala -> Sthanabala -> Saptavargajabala** : This section computes strength of planets in the chart in virupas based on its position in 7 divisional charts. 
        - **Balas -> Shadbala -> Sthanabala -> Ojhayugmarashiamshabala** : A planet gains strength because it is in an even or uneven sign or navamsa. this strength is computed for all 7 planets and this section is updated. 
        - **Balas -> Shadbala -> Sthanabala -> Kendradhibala** : The planetery strength based on placement in kendra or different houses is computed for all 7 planets and updated here.
        - **Balas -> Shadbala -> Sthanabala -> Drekshanabala** : The drekshana bala is comnputed for all 7 planets based on its position in 1/3rd of the signs as described by parashara and updated here.
        - **Balas -> Shadbala -> Sthanabala -> Total** : Total of Sthanabala for each of 7 planet is given here 
    - **Balas -> Shadbala -> Digbala** : This is the directional strength of 7 planets which are computed and updated here. 
    - **Balas -> Shadbala -> Kaalabala** : These are time based strengths for all 7 planets computed and updated. 
        - **Balas -> Shadbala -> Kaalabala -> Natonnatabala**
        - **Balas -> Shadbala -> Kaalabala -> Pakshabala**
        - **Balas -> Shadbala -> Kaalabala -> Tribhagaabala**
        - **Balas -> Shadbala -> Kaalabala -> Varsha-maasa-dina-horabala**
        - **Balas -> Shadbala -> Kaalabala -> Yuddhabala**
        - **Balas -> Shadbala -> Kaalabala -> Ayanabala**
        - **Balas -> Shadbala -> Kaalabala -> Total**
    - **Balas -> Shadbala -> Cheshtabala** : This is motional strength of planet which is computed for all 7 planets and updated here.
    - **Balas -> Shadbala -> Naisargikabala** : This is Natural strength of planet which is computed for all 7 planets and updated here.
    - **Balas -> Shadbala -> Drikbala** : This is Aspect based strength of planet which is computed for all 7 planets and updated here.
    - **Balas -> Shadbala -> Total** : This is sum of all sub strength of planet in virupas which is computed for all 7 planets and updated here.
    - **Balas -> Shadbala -> Rupas** : This is sum of all sub strength of planet but in rupas which is computed for all 7 planets and updated here.
- **Balas -> Ishtabala/Kashtabala** : These are the planetery strengths derived from shadbala for all 7 planets. 60 virupas are divided between ishtabala and kashtabala. If ishtabala is more then planet does good or else it gives problems. These balas are updated for all 7 planets in its respective sections.
- **Balas -> Bhavabala** : This is strength of houses. All 12 houses get different strengths in virupas which is sum of 3 sub strengths.Each subsection is array of 12 elements. first element is for first house and similarly last element is for 12th house. The subsections are given below: 
    - **Balas -> Bhavabala -> BhavaAdhipathibala** : This is the shadbala of lord of the house. 
    - **Balas -> Bhavabala -> BhavaDigbala** : This is the Directional strength of sign in the house
    - **Balas -> Bhavabala -> BhavaDrishtibala** : This is the Aspectual strength of planets on the house
    - **Balas -> Bhavabala -> Total** : This is the sum of all 3 sub balas of the house. 

### user_details Data:
This Section contains various panchanga details when the person was born. The sub sections are
- **user_details -> name** : Name of the person
- **user_details -> birthdetails** : The birth data given are stored here in below format
    - **user_details -> birthdetails -> DOB** : Date of Birth details
        - **user_details -> birthdetails -> DOB -> year** : birth year
        - **user_details -> birthdetails -> DOB -> month** : birth month
        - **user_details -> birthdetails -> DOB -> day** : birth day
    - **user_details -> birthdetails -> TOB** : Time of Birth details
        - **user_details -> birthdetails -> TOB -> hour** : birth hour in 24 hour format
        - **user_details -> birthdetails -> TOB -> min** : birth minute part
        - **user_details -> birthdetails -> TOB -> sec** : birth second part
    - **user_details -> birthdetails -> POB** : Place of Birth details
        - **user_details -> birthdetails -> POB -> name** : Name of birth place
        - **user_details -> birthdetails -> POB -> lat** : lattitude of birth place
        - **user_details -> birthdetails -> POB -> lon** : longitude of birth place
        - **user_details -> birthdetails -> POB -> timezone** : GMT timezone of birth place
    - **user_details -> birthdetails -> Gender** : Gender of the person : "male", "female", "other"
    - **user_details -> birthdetails -> name** : name of the person 
- **user_details -> maasa** : month of birth as per hindu calender
- **user_details -> vaara** : weekday of birth as per hindu calender
- **user_details -> tithi** : day of month of birth as per hindu calender
- **user_details -> karana** : karana of birth as per hindu calender
- **user_details -> nakshatra** : Moon was in which nakshatra when the person was born
- **user_details -> yoga** : yoga of birth as per hindu calender
- **user_details -> rashi** : what is the rashi(moon sign) of the person

---
---

This can be used to develop indian astrology applications and softwares on top of this. 

For this module to work you need **Python version 3+**

Other modules needed for this to work is only pyswisseph: 
``` 
pip install pyswisseph==2.8.0.post1
```

Github repository for this module: https://github.com/VicharaVandana/jyotishyamitra.git 

For jyotishyamitra package : [Click Here](https://pypi.org/project/jyotishyamitra/)
        
        
        

    
     
    
    
    
    
        
        
        
        
        










