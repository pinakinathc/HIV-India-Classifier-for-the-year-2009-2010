import os
print "Execution started, Please wait..."
os.system('python data_initializer.py')
os.system('python semi_classifier.py')
os.system('python main_classifier.py')
print "Execution over...Thank you for your time."