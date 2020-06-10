<img
              class="img-fluid pic"
              src="https://github.com/jayanthj737/worth-a-read/blob/master/static/images/icon.png"
              height="30%"
              width="30%"
            />
# Worth-a-read
NLP based Extractive Text Summarizer uses nltk python package and backend in flask to be easily compatible with .py files.
<h2 class="topic" style="color: rgb(197, 163, 163);">
          What is Natural language Processing (NLP) ?
        </h2>
        <p>
          Natural Language Processing or NLP is a field of Deep Learning that
          helps computers understand, interpret and manipulate human language.
          Natural language processing helps computers communicate with humans in
          their own language and scales other language-related tasks. For
          example, NLP makes it possible for computers to read text, hear
          speech, interpret it, measure sentiment and determine which parts are
          important.
        </p>
        <hr />
        <h2 class="topic" style="color: rgb(197, 163, 163);">Why NLP ?</h2>
        <p>
          Natural Language Processing is present everywhere, the news-apps give
          a gist of the news as a preview which uses these NLP models to render
          a short crisp idea of the news. Unlike Image based models using CNNs
          or any other Neural Networks its not as easy to process data, as in
          the case of images we have the pixel data as numbers, but in the case
          of words or sentences we cannot convert each of them into their ASCII
          equivalent everytime.
        </p>
        <hr />

 <h2 class="topic" style="color: rgb(197, 163, 163);">
          What is Text Summarization ?
        </h2>
        <p>
          Summarization is basically producing a short idea from a large piece
          of information without affecting the meaning or the take away of the
          text. So it depends on how a model treats which part of the text is
          important and which can be neglected as a whole. Therefore we have two
          types of Summarization Techniques namely:
        </p>
        <h5 class="topic" style="color: rgb(197, 163, 163);">
          <strong>Abstractive Text Summarization </strong>
        </h5>
        <p>
          Abstractive methods contains words that needn't be present in the
          source documents. These select words based on semantic understanding,
          It helps in bringing out a new and consise idea by understanding the
          text. They interpret and examine the text using advanced natural
          language techniques in order to generate a new shorter text that
          conveys the most critical information from the original text.
          Therefore, we can say that Abstractive text Summarization is closely
          related to human semantics understanding capabilities.
        </p>
        <h5 class="topic" style="color: rgb(197, 163, 163);">
          <strong>Extractive Text Summarization </strong>
        </h5>
        <p>
          Extractive methods helps in summarizing articles by selecting a set of
          common or reduntant words which gives the idea of the main text. In a
          way it assigns certain weight to certain parts or words in a sentence
          and then helps in giving necessary information. Abstractive text
          summarization requires high level of training so commonly we use
          extractive Summarization techniques. The extraction is made according
          to the defined metric without making any changes to the texts.
          <span><br /> </span>
          In this projectExtractive Text Summarization techniques are used to
          summarize given texts.
        </p>
        <hr />
        <h2 style="color: rgb(197, 163, 163);">
          <strong>How do we do Extractive Text summarization? </strong>
        </h2>
        <p>
          We make use of the NTKL toolkit provided by Python. The Natural
          Language Toolkit, or more commonly NLTK, is a suite of libraries and
          programs for symbolic and statistical natural language processing for
          English written in the Python programming language.
        </p>
        <h4 style="color: rgb(197, 163, 163);">
          <strong>I. Create a Hash table with frequencies of each word.</strong>
        </h4>
        <p>
          A dictionary is created with the frequency of occurence of each word
          in the given text. One this we should do is to avoid the stopWords,
          which are the commonly used words like a, an, the, so on.
          <span><br /> </span>
          To avoid the stopWords we can use the nltoolkit's stopWords method,
          which ignores the earlier mentioned commonly used words.
          <span><br /> </span>
          <span>
            <img
              class="img-fluid pic"
              src="https://github.com/jayanthj737/worth-a-read/blob/master/static/images/2.png"
              height="73%"
              width="73%"
            />
          </span>
          <span><br /> </span>
        </p>
        <h4 style="color: rgb(197, 163, 163);">
          <strong>II. Tokenize the given Text.</strong>
        </h4>
        <p>
          We split each sentence using the nltoolkit's tokenizer and thus get a
          vector of sentences/string, which can be further used to score each
          sentence according to the frequency count.
          <span><br /> </span>
          <span
            ><img
              class="img-fluid pic"
              src="https://github.com/jayanthj737/worth-a-read/blob/master/static/images/1.png"
              height="73%"
              width="73%"
            />
          </span>
          <span><br /> </span>
        </p>
        <h4 style="color: rgb(197, 163, 163);">
          <strong
            >III. Score each sentence according to the frequency table
            count.</strong
          >
        </h4>
        <p>
          A sentence is scored according to the frequence of count of the
          non-stopWords by running to loops on the sentence vector and also on
          the Hash Table.
          <span><br /> </span>
          This gives us the score for further sentence formation.
          <span><br /> </span>
          <span
            ><img
              class="img-fluid pic"
              src="https://github.com/jayanthj737/worth-a-read/blob/master/static/images/3.png"
              height="73%"
              width="73%"
            />
          </span>
          <span><br /> </span>
        </p>
        <h4 style="color: rgb(197, 163, 163);">
          <strong
            >IV. Use a Max Heap or a priority Queue to get highly scored
            sentences</strong
          >
        </h4>
        <p>
          We make use of Max heap to get the sentences with higher scores, and
          construct a final piece of text using the same.active
          <span><br /> </span>
          Thus, providing us with the final summary of the given text.
          <span><br /> </span>
          <span>
           <img
              class="img-fluid pic"
              src="https://github.com/jayanthj737/worth-a-read/blob/master/static/images/4.png"
              height="73%"
              width="73%"
            />
          </span>
          <span><br /> </span>
        </p>
        <p>This is how NLP can be used for TEXT Summarization.</p>
        <h2 class="topic" style="color: rgb(197, 163, 163);">
          Sample
        </h2>
        <span><br /> </span>
        <div class="row text-center">
          <div class="col-lg-6">
            <h2 class="topic" style="color: rgb(197, 163, 163);">
              Actual text
            </h2>
           <img
              class="img-fluid pic"
              src="https://github.com/jayanthj737/worth-a-read/blob/master/static/images/long.png"
              height="73%"
              width="73%"
            />
          </div>
          <div class="col-lg-6">
            <h2 class="topic" style="color: rgb(197, 163, 163);">
              Summarized text
            </h2>
           <img
              class="img-fluid pic"
              src="https://github.com/jayanthj737/worth-a-read/blob/master/static/images/short.png"
              height="73%"
              width="73%"
            />
          </div>
        </div>
      </div>
