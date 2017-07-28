import os
print "Execution started, Please wait..."
os.system('python data_initializer.py')
os.system('python semi_automated.py')
os.system('python main_classifier.py')
print "Execution over...Thank you for your time."