from flask import Flask, render_template, request
from gensim.models.ldamodel import LdaModel
from gensim.parsing.preprocessing import preprocess_string, remove_stopwords, strip_tags, strip_punctuation, strip_numeric
from gensim.corpora.dictionary import Dictionary
from gensim.utils import tokenize
import spacy as sp
from spacy.lang.en import English
import pickle

'''preporcessing'''
nlp = English()
nlp = sp.load("en_core_web_md")

'''previous model'''
#lda_mod = LdaModel.load('lda_final.model') #0-people and society, 1-climate change, 2-politics
#loaded_dict = Dictionary.load('mix_P_dic')

#with open('mix_P', "rb") as fp:  # Unpickling
#    loaded_crp = pickle.load(fp)

'''start applicaiton'''
application = Flask(__name__)

@application.route('/',methods=["GET","POST"])
def home():
    if request.method == "POST":
        text_input = request.form["nm"]

        '''preprocess text
        
        CUSTOM_FILTERS = [lambda x: x.lower(), strip_tags, strip_punctuation, remove_stopwords, strip_numeric]
        pp_txt = preprocess_string(text_input, CUSTOM_FILTERS)
        npp_txt = list(tokenize(text_input.lower()))
        nlp_art = nlp(str(pp_txt))
        art = [token.lemma_ for token in nlp_art if token.pos_ == 'NOUN' or token.pos_ == 'VERB']

        nlp_art = ' '.join(art)
        nlp_art = nlp(nlp_art)
        nchunk = []
        for chunk in nlp_art.noun_chunks:
            if len(chunk) > 1 and len(chunk) <= 3:
                nchunk.append(chunk.text)

        art = nchunk + art

        new_text_corpus = loaded_dict.doc2bow(art)

        m = lda_mod.get_document_topics(new_text_corpus, 0)

        labels = ['Breaking News', 'Climate Change', 'Politics']
        values =[row[1] for row in m if row[0] <3]'''

        '''removed text'''
        #rmvd_txt =  [txt for txt in npp_txt if txt not in pp_txt]
        labels = ['Breaking News', 'Climate Change', 'Politics']
        values = [0.5,0.5,0.5]
        rmvd_txt = "words"


        return render_template('index.html')
    else:
        return render_template("index.html", content="Testing")

if __name__ == "__main__":
    application.run(debug=True)
