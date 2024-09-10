from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, AutoModelForSequenceClassification, T5ForConditionalGeneration, BertForMaskedLM, AutoModelForTokenClassification

class TextGenerationModel:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        if 't5' in model_name:
            self.model = T5ForConditionalGeneration.from_pretrained(model_name)
        elif 'bert' in model_name:
            self.model = BertForMaskedLM.from_pretrained(model_name)
        else:
            self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def generate(self, prompt, max_length=100):
        return self.generator(prompt, max_length=max_length, num_return_sequences=1)[0]['generated_text']

class SentimentAnalysisModel:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.classifier = pipeline("sentiment-analysis", model=self.model, tokenizer=self.tokenizer)

    def analyze(self, text):
        result = self.classifier(text)[0]
        return {
            "sentiment": result['label'],
            "score": result['score']
        }

class NERModel:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForTokenClassification.from_pretrained(model_name)
        self.ner = pipeline("ner", model=self.model, tokenizer=self.tokenizer, aggregation_strategy="simple")

    def extract_entities(self, text):
        return self.ner(text)

# Initialize models
text_generation_models = {
    'gpt2': TextGenerationModel('gpt2'),
    'bert': TextGenerationModel('bert-base-uncased'),
    't5': TextGenerationModel('t5-small')
}

sentiment_analysis_models = {
    'bert': SentimentAnalysisModel('bert-base-uncased-finetuned-sst-2-english'),
    'roberta': SentimentAnalysisModel('roberta-base-sentiment'),
    'distilbert': SentimentAnalysisModel('distilbert-base-uncased-finetuned-sst-2-english')
}

ner_models = {
    'spacy': NERModel('spacy_pretrained_pipelines'),
    'flair': NERModel('flair/ner-english-ontonotes-large'),
    'stanford': NERModel('stanfordnlp/ner-bert-base-uncased')
}

def get_text_generation_model(model_name):
    return text_generation_models.get(model_name, text_generation_models['gpt2'])

def get_sentiment_analysis_model(model_name):
    return sentiment_analysis_models.get(model_name, sentiment_analysis_models['bert'])

def get_ner_model(model_name):
    return ner_models.get(model_name, ner_models['spacy'])