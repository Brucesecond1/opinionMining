# Airton Bordin Junior
# airtonbjunior@gmail.com
# Federal University of Goias (UFG)
# Computer Science Master's Degree

from nltk.corpus import stopwords
from datetime import datetime

# Paths
SEMEVAL_TRAIN_FILE = 'datasets/train/twitter-train-cleansed-B.txt'
SEMEVAL_TEST_FILE  = 'datasets/test/SemEval2014-task9-test-B-all-tweets_withSVMValues.txt'
STS_TRAIN_FILE = 'datasets/train/STS/STStrain.1600000.processed.noemoticon.EDITED.csv'
STS_TEST_FILE = 'datasets/test/STS/STS_Gold_All.txt'
DICTIONARY_POSITIVE_WORDS = 'dictionaries/positive-words.txt'
DICTIONARY_NEGATIVE_WORDS = 'dictionaries/negative-words.txt'
DICTIONARY_POSITIVE_HASHTAGS  = 'dictionaries/positive-hashtags.txt'
DICTIONARY_NEGATIVE_HASHTAGS  = 'dictionaries/negative-hashtags.txt'
DICTIONARY_POSITIVE_EMOTICONS = 'dictionaries/positive-emoticons.txt'
DICTIONARY_NEGATIVE_EMOTICONS = 'dictionaries/negative-emoticons.txt'
DICTIONARY_NEGATING_WORDS = 'dictionaries/negating-word-list.txt'
DICTIONARY_BOOSTER_WORDS = 'dictionaries/boosterWords.txt'
DICTIONARY_SENTIWORDNET = 'dictionaries/SentiWordNet_3.0.0_20130122.txt'
DICTIONARY_AFFIN = 'dictionaries/affin.txt'
DICTIONARY_SLANG = 'dictionaries/slangSD.txt'
DICTIONARY_VADER = 'dictionaries/vaderLexicon.txt'
DICTIONARY_SEMEVAL2015  = 'dictionaries/SemEval2015-English-Twitter-Lexicon.txt'
DICTIONARY_EFFECT  = 'dictionaries/EffectWordNet.tff'
#DICTIONARY_EFFECT  = 'dictionaries/goldStandard.tff'

TRAIN_WORDS = 'datasets/train/words_train/words_train.txt'
TEST_WORDS  = 'datasets/test/words_test.txt'

BEST_INDIVIDUAL 		 = 'partial-best-individual ' + str(datetime.now())[11:13] + str(datetime.now())[14:16] + str(datetime.now())[17:19] + '.txt'
BEST_INDIVIDUAL_2CLASSES = 'partial-best-individual-2classes ' + str(datetime.now())[11:13] + str(datetime.now())[14:16] + str(datetime.now())[17:19] + '.txt'

model_results = []

all_train_words = []
all_test_words  = []

use_svm_neutral 	  		= False
use_url_to_neutral	  		= False
use_date_to_neutral         = False
use_url_and_date_to_neutral = False
use_emoticon_analysis 		= True
use_only_gp 	      		= False
use_only_svm		  		= False

neutral_inferior_range = 0
neutral_superior_range = 0

liu_weight       	= 1
sentiwordnet_weight = 1
affin_weight        = 1
vader_weight        = 1
slang_weight        = 1
effect_weight       = 1
semeval2015_weight  = 1

# True: load the dictionary
use_dic_liu          = True
use_dic_sentiwordnet = True
use_dic_affin        = True
use_dic_vader        = True
use_dic_slang        = True
use_dic_effect       = True
use_dic_semeval2015  = True

# Check if the dictionary was loaded
dic_liu_loaded 			= False
dic_sentiwordnet_loaded = False
dic_affin_loaded		= False
dic_vader_loaded		= False
dic_slang_loaded		= False
dic_effect_loaded		= False
dic_semeval2015_loaded	= False

dic_loaded_total = 0

# Balance the train tweets
MAX_POSITIVES_TWEETS = 3000
MAX_NEGATIVES_TWEETS = 3000
MAX_NEUTRAL_TWEETS   = 1500

# GP Parameters
CROSSOVER   = 0.9
MUTATION    = 0.1
#MUTATION_W  = 0.75
MUTATE_EPHEMERAL = 0.75
GENERATIONS = 150
POPULATION  = 300
cicles_unchanged = 0
generations_unchanged = 0
max_unchanged_generations = 250
max_unchanged_cicles = 9999999999

root_constraint = True
root_function = "polaritySumAVGUsingWeights"
#root_function = "polaritySumAVG"
#root_functions = ["polaritySumAVGUsingWeights", "if_then_else"]
root_decreased_value = 0.2

massive_functions_constraint = True
massive_function = "polaritySumAVGUsingWeights"
massive_functions_max = 1

neutral_range_constraint = True

generations_unchanged_reached_msg = False

TOTAL_MODELS = 5

#  
FILE_RESULTS  = 'test_results-' + str(datetime.now())[11:13] + str(datetime.now())[14:16] + str(datetime.now())[17:19] + '.txt'
FILE_RESULTS_2CLASSES  = 'test_results-2classes' + str(datetime.now())[11:13] + str(datetime.now())[14:16] + str(datetime.now())[17:19] + '.txt'

TRAIN_RESULTS = 'train-' + str(TOTAL_MODELS) + 'models_' + str(POPULATION) + 'p'+ str(GENERATIONS) +'g_' + str(datetime.now())[11:13] + str(datetime.now())[14:16] + str(datetime.now())[17:19] + '.txt'
TRAIN_RESULTS_2CLASSES = 'train-' + str(TOTAL_MODELS) + 'models_2classes_' + str(POPULATION) + 'p'+ str(GENERATIONS) +'g_' + str(datetime.now())[11:13] + str(datetime.now())[14:16] + str(datetime.now())[17:19] + '.txt'

tweets_semeval        = []
tweets_semeval_score  = []
svm_values_tweets     = []
svm_is_neutral        = []
svm_normalized_values = []
tweet_semeval_index   = 0

tweets_sts       = []
tweets_sts_score = []

tweets_sts_test       = []
tweets_sts_score_test = []

tweets_sts_positive = 0
tweets_sts_negative = 0

# All are converted into sets because we don't need to keep the order
dic_positive_words     = []
dic_negative_words     = []
dic_positive_hashtags  = []
dic_negative_hashtags  = []
dic_positive_emoticons = []
dic_negative_emoticons = []
dic_negation_words     = []
dic_booster_words      = []

# Using python dictionary to improve the search performance
dic_positive_semeval2015  = {}
dic_negative_semeval2015  = {}

dic_positive_slang        = {}
dic_negative_slang        = {}

dic_positive_affin        = {}
dic_negative_affin        = {}

dic_positive_sentiwordnet = {}
dic_negative_sentiwordnet = {}

dic_positive_effect       = {}
dic_negative_effect       = {}

dic_positive_vader        = {}
dic_negative_vader        = {}

# Counters
positive_tweets = 0
negative_tweets = 0
neutral_tweets  = 0

fitness_positive = 0
fitness_negative = 0
fitness_neutral  = 0

# Save the best values 
best_fitness = 0
best_fitness_history  = []
best_fitness_per_generation_history = []
all_fitness_history   = []

best_accuracy = 0

best_precision_positive = 0
best_precision_negative = 0
best_precision_neutral  = 0
best_precision_avg      = 0

best_recall_positive = 0
best_recall_negative = 0
best_recall_neutral  = 0
best_recall_avg      = 0

best_f1_positive = 0
best_f1_negative = 0
best_f1_neutral  = 0
best_f1_avg      = 0
best_f1_positive_negative_avg = 0

best_precision_avg_function = ""
best_recall_avg_function    = ""
best_f1_avg_function        = ""

precision_positive_history = []
precision_negative_history = []
precision_neutral_history  = []
recall_positive_history    = []
recall_negative_history    = []
recall_neutral_history     = []
f1_positive_history        = []
f1_negative_history        = []
f1_neutral_history         = []

tweets_mukh = []
tweets_mukh_score = []
tweets_mukh_positive = 0
tweets_mukh_negative = 0

tweets_2013       = []
tweets_2013_score = []
tweets_2013_positive = 0
tweets_2013_negative = 0
tweets_2013_neutral  = 0

tweets_2014       = []
tweets_2014_score = []
tweets_2014_positive = 0
tweets_2014_negative = 0
tweets_2014_neutral  = 0

tweets_liveJournal2014       = []
tweets_liveJournal2014_score = []
tweets_liveJournal2014_positive = 0
tweets_liveJournal2014_negative = 0
tweets_liveJournal2014_neutral  = 0

tweets_2014_sarcasm       = []
tweets_2014_sarcasm_score = []
tweets_2014_sarcasm_positive = 0
tweets_2014_sarcasm_negative = 0
tweets_2014_sarcasm_neutral  = 0

sms_2013       = []
sms_2013_score = []
sms_2013_positive = 0
sms_2013_negative = 0
sms_2013_neutral  = 0

all_messages_in_file_order = []
all_polarities_in_file_order = []

MAX_ANALYSIS_TWEETS = 10000

false_neutral_log  = 0
false_negative_log = 0
false_positive_log = 0

log_all_metrics_each_cicle = False
log_all_messages           = False
log_parcial_results        = True
log_times           	   = True
log_loads                  = True


save_file_results = True

stop_words = set([x.lower() for x in stopwords.words('english')])

week_dates  = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
month_dates = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'jan', 'feb', 'mar', 'apr', 'may', 'june', 'july', 'aug', 'sept', 'oct', 'nov', 'dec']
other_dates = ['tomorrow', 'yesterday', 'today']

all_dates = week_dates + month_dates + other_dates