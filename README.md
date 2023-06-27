# Yahoo Finance data downloader

* Fetchs data from yahoo finance website for the given inputs and save in a csv file. https://finance.yahoo.com/quote/TATAPOWER.NS/history?p=TATAPOWER.NS
 
* Inputs:
    * symbol - Symbol name
    * start and end dates formats would be yyyy-dd-mm
    * interval would be one of '1d', '1wk', '1mo'
    * events would be one of 'history', 'div', 'split', 'capitalGain'
    * adjusted would be either true or false
    * download would be folder in which files to be saved. if no input provided then it downloads where python script is located. 

* Outputs:
    * Output file name would be <%Y%m%d%H%M%S>_<symbol>.csv file 

* Sample command 
    * python dnld_yhoo_hist.py --symbol <symbolname> --start <startdate> --end <enddate> --interval <interval> --events <history>  --adjusted <true/false>
    * Example: python dnld_yhoo_hist.py --symbol TATAMOTORS.NS --start 2023-06-01 --end 2023-07-08 --interval 1d --events history  --adjusted true

* Download Class Usage in another python scripts
    * from dnld_yhoo_hist import Download 
    * Create reference to Download class and call run method
        * ref = Download()
        * ref.run()