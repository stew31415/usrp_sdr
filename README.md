# usrp_sdr
This project is used to analyze, in real time, wideband scan using USRP. Builds upon usrp_spectrum_sense.py from https://github.com/gnuradio/gnuradio/blob/master/gr-uhd/examples/python/usrp_spectrum_sense.py

usrp_spectrum_sense_output.py: Minor change has the original program output data to a .txt file. User can specify name of file in code (file name assignement is near bottom of code).

usrp_plotter.py: Program that plots data coming into .txt file from usrp_spectrum_sense_output.py. 2dhist x bins is arbitrary value to make the plots I had look better. ylim and y bins are set at 100 because I was scanning a 100MHz band and wanted a bin for each 1 MHz band. User can change name of input file at top of code.
