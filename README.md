This library read text document and returns the classification of this document based on Json predefined tree.

To install:

<pre>

git clone git@github.com:gtoutoungis1/flavors.git

cd flavors

sudo python setup.py install
</pre>

In Python Shell:

import flavors

flavors provide 3 methods:

traverse : walk the Json tree file, this file presents the Wheel flavors data

score : use fuzzywuzzy library to define the score of a word in a text by using list of word choices.

run : use as flavors.run(wheel_file, tasting_file).
	this is the main method that's calling the traverse method with the wheel_file, and the score method with the tasting_file.

	The docs directory contains an example of the required files.

The flavors library return the /tmp/categories.html file, here is an example of the content of the output file:

	"An excellent cup of coffee. Notes of stone fruit, cherry and plum. Long finish with hints of milk chocolate and brown sugar."`


	<pre>
	[
	    ["Fruity", "Other Fruit", "Cherry"],
	    ["Sweet", "Brown Sugar"],
	    ["Nutty/Cocoa", "Cocoa", "Chocolate"]
	]
	</pre>


The flavors library return all matching words wich their score is more than the score's average, and it is not equal to 0.




