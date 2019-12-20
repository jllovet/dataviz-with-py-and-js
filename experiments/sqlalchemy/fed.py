
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

''' Demonstrating an economic concern with the central bank money printing:

The problem is analogous to an example where Company A (say, Raytheon) wants to loan its products to another Company B
(say, Southwest Airlines) for some purpose.  Rather than loaning them the products, Raytheon creates new shares for 
ownership of its company and loans those to Southwest Airlines so that Southwest Airlines can sell those shares to pay 
for Raytheon's products.  But this lowers the value of the shares all of the other shareholders hold.

Similarly with a central bank printing money, the value of the shares (dollars) that all of the other shareholders hold 
(the public) lose value, but the primary difference is that here there is a delay in the market reflecting these changes
in value.  Whoever receives this newly printed money first has the privilege of spending this money before the market 
reflects the decrease in the value of the dollar.  And who receives this money before they trickle down to the public?  
The government and its clients, namely corporations.  It would be as if Raytheon created these new shares and loaned 
them to Southwest Airlines to sell off before the other shareholders realized that the new shares were created.
'''

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    company = Column(String(32))

    equity = Column(Integer)
    total_shares = Column(Integer)

class Holding(Base):
    __tablename__ = 'holdings'

    id = Column(Integer, primary_key=True)
    shareholder = Column(String(32))

    company = Column(String(32))
    shares = Column(Integer)

# create tables
engine = create_engine('mysql+pymysql://root:root@localhost/temp', echo=False) # mysql+pymysql = dialect + driver name
#Company.__table__.drop(engine) # delete table
#Holding.__table__.drop(engine) # delete table
Base.metadata.create_all(engine)

# add session to interact with DB
Session = sessionmaker(bind=engine)
session = Session()

# data
companies = [
    {'company': 'NWO',
     'equity': 1000000, # 1 Million
     'total_shares': 1000 # 1 Thousand
     }
]

holdings = [
    {'shareholder': 'NWO',
     'company': 'NWO',
     'shares': 600,
     },
    {'shareholder': 'Hegel',
     'company': 'NWO',
     'shares': 400,
     }
]

# add data to DB
holdings_rows = [Holding(**h) for h in holdings] # ** unpacks the argument into key/value pairs
session.add_all(holdings_rows)
session.add(Company(**companies[0]))
session.commit()

# determine value of shares held
def calculate_share_portion_value(shares, company):
    company_row = session.query(Company).filter(Company.company == company).first()
    share_value = company_row.equity*(shares/company_row.total_shares)
    return share_value

# print value of shares for each holder
def print_holdings():
    print("Holdings:")
    for holding in session.query(Holding):
        share_value = calculate_share_portion_value(holding.shares, holding.company)
        print("\t%s owns %d shares in %s (Value: %d)"\
              %(holding.shareholder, holding.shares, holding.company, share_value))

print_holdings()

# NWO creates new shares to lend to Marx to sell off in order to buy supplies for the revolution
nwo = session.query(Company).filter(Company.company == 'NWO').first()
nwo.total_shares += 250

marx = {
    'shareholder': 'Marx',
    'company': 'NWO',
    'shares': 250
}
session.add(Holding(**marx))

session.commit()

print_holdings()