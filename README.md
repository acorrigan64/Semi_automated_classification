<h1 align="center">
Multi-Label Classification Of Medical Texts
</h1>

The Learning from Death morality Review (LeDeR) is an organisation focused on the reviewing of death reports for people with learning disabilities, this involves manually coding death reports with pre-determined labels a time consuming process. Here a program is proposed that suggests labels for the text based on a supervised learning algorithm (an SVM), the human coder can then reject or select the label based on the programs suggestions.

**Aims of Project**
<ul>
  <li>Increase the accuracy of coders</li>
  <li>Reduce the time taken to code a doccument</li>
  <li>Provide human interpretable coding suggestions</li>
  <li>Be implementable with minimum training</li>
</ul>


**Approach**
SVMs were chosen as they have been found to achieve state of the art performance for NLP classification tasks. TF-IDF and word vectorisation approaches were compared and similar accuracies were achieved.
This model and vectorisers was then exported and used for a simple TKinter text based interface.


**Results**
Due to caronavirus the effectiveness of the program was not able to be tested with the LeDeR coders however previous research into semi-automated classification prgrams the aacuracy threshold for improvement on time and accuracy was reached. The future works section of the report outlines how the tests should be carried out.


The report detailing all aspects of the project can be viewed [here](/report.pdf).


The project involved the use of the following technologies:

- Python
- Pandas
- sklearn
- TQDM
- TKinter
- SVMs
- Word2vec
- Matplotlib
