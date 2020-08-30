# PurBeurre_P8
Openclassrooms DA-Python P8 Pur Beurre: 
Créez une plateforme pour amateurs de Nutella

### Create a web platform to find healthy substitutes to excessively fatty, over-sweetened or over-salted foods

### Constraints
> tests included in the project

> use of PostgreSql to deploy the project with Heroku

> include a page with "Mentions Légales"

> PEP8 compliant

> Github versioning

> code written in english

> agile methodology

### How to use this program

> You can find this program deployed on Heroku : ******

> You can also fork this repository :
```bash
git clone "https://github.com/elwaze/PurBeurre_P8.git"
```

> Use requirements.txt to install the program environment:
```bash
pip install -r requirements.txt
```

> Setting environment variables 
```bash
*****
```

### Testing

#### Coverage

**Remove coverage_html_report folder** to ensure no previous generated files remains.

**.coveragerc** file has been created to finely tune the coverage behavior.

```bash
cd PurBeurre_P8/pur_beurre
coverage erase
coverage run manage.py test --settings=pur_beurre.test_settings
coverage 
```

... to be continued


