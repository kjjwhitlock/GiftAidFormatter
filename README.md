# Gift Aid Formatter #

This script takes data exported from the Philantro platform, formats it and exports it to a new CSV file that is compliant with the [HMRC Gift Aid schedule.](https://www.gov.uk/guidance/schedule-spreadsheet-to-claim-back-tax-on-gift-aid-donations)

It does this by:
* Filtering for donors that have confirmed they'd like to gift aid 
* Adding (empty) columns for Title, Aggregated Donations and Sponsored Event
* Replacing international postcodes with 'X'
* Limited street address to 40 characters 
* Formatting postcodes to include a middle space

## TO RUN ## 

Ensure you have python 3+ and pandas installed (`pip install pandas`) and then run the script on the command line:

`python main.py`

## THEN ## 

You will then need to copy and paste the outputed data into your giftaid schedule downloadable at the link above. 


*Made with :heart: for TAP London.*