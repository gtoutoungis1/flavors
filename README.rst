This library read text document and returns the classification of this document based on Json predefined tree.

To install:

git clone https://github.com/gtoutoungis1/flavors/

In Python Shell:

import flavors

flavors provide 3 methods:

traverse : walk the Json tree file, this file presents the Wheel flavors data

score : use fuzzywuzzy library to define the score of a word in a text by using list of word choices.

run : use as flavors.run(wheel_file, tasting_file).
	this is the main method that's calling the traverse method with the wheel_file, and the score method with the tasting_file.

The flavors library return the /tmp/categories.html file, here is an example of the content of the output file:

	"An excellent cup of coffee. Notes of stone fruit, cherry and plum. Long finish with hints of milk chocolate and brown sugar."`

	the library *might* return the following categories:

	<pre>
	[
	    ["Fruity", "Other Fruit", "Cherry"],
	    ["Sweet", "Brown Sugar"],
	    ["Nutty/Cocoa", "Cocoa", "Chocolate"]
	]
	</pre>


The flavors library return all matching words with score more that the score's average, for all scores with value more than 0.




