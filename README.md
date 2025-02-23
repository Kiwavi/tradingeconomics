# tradingeconomics
TRADING ECONOMICS - API Code Examples

## Get Started    
Clone this repository into a directory    
Assuming you're in the folder already    
`git clone https://github.com/Kiwavi/tradingeconomics.git .    `    
Create a virtual environment    
`python -m venv venv    `    
Activate the virtual environment       
`source venv/bin/activate    `    
Install required packages    
`pip install -r requirements.txt    `    
Migrate    
`python manage.py migrate    `    
Run the server    
`python manage.py runserver    `    
Visit http://127.0.0.1:8000/ in your browser    
### Tech stack    
- Python (Django)    
- Javascript    
- TailwindCSS    
- HTML    
### Features    
- Data fetched from Tradingeconomics API and organized inside a table.    
- Chart Comparison between two countries with update option available.        
- Ability to update charts based on number of years(flexible for any number of years based on all years available in the data)        
