import time

from variables import *
from functions import *

# log time
start = time.time()


if __name__ == "__main__":
    getDictionary()

    # baseline
    function_to_evaluate = "if_then_else(hasEmoticons(x), emoticonsPolaritySum(removeLinks(x)), polaritySum(removeEllipsis(removeLinks(lemmingText(removeAllPonctuation(replaceNegatingWords(x)))))))"


    # other functions tested
    #function_to_evaluate = "add(invertSignal(negativeWordsQuantity(x)), sin(polaritySum(x)))"
    #function_to_evaluate = "sub(mul(sub(polaritySum(removeStopWords(stemmingText(x))), sin(-0.3012931295024437)), protectedLog(-0.21199248533470838)), protectedLog(protectedLog(sub(polaritySum(stemmingText(stemmingText(stemmingText(removeStopWords(removeStopWords(removeStopWords(stemmingText(removeStopWords(stemmingText(removeStopWords(x))))))))))), sub(hashtagPolaritySum(removeStopWords(removeStopWords(removeStopWords(x)))), cos(protectedLog(polaritySum(stemmingText(removeStopWords(removeStopWords(x)))))))))))"
    #function_to_evaluate = "mul(add(add(polaritySum(repeatInputString(repeatInputString(repeatInputString(repeatInputString(repeatInputString(repeatInputString(repeatInputString(repeatInputString(repeatInputString(repeatInputString(repeatInputString(x)))))))))))), positiveEmoticons(repeatInputString(repeatInputString(repeatInputString(repeatInputString(repeatInputString(repeatInputString(x)))))))), mul(sub(sin(-0.7500287440821918), protectedDiv(negativeEmoticons(repeatInputString(repeatInputString(repeatInputString(repeatInputString(repeatInputString(repeatInputString(x))))))), protectedSqrt(protectedDiv(protectedLog(0.30225574066002103), cos(0.3289974105155071))))), protectedDiv(sin(negativeWordsQuantity(repeatInputString(repeatInputString(repeatInputString(repeatInputString(x)))))), add(protectedSqrt(cos(mul(hashtagPolaritySum(x), -1.1631941015415768))), -0.27062630818833844)))), mul(protectedDiv(protectedLog(-0.9481590665673725), negativeEmoticons(x)), exp(add(-0.28621032356521914, -0.21595094634073808))))"
    #function_to_evaluate = "add(emoticonsPolaritySum(repeatInputString(repeatInputString(repeatInputString(repeatInputString(repeatInputString(x)))))), polaritySum(repeatInputString(repeatInputString(repeatInputString(repeatInputString(x))))))"
    #function_to_evaluate = "if_then_else(hasEmoticons(removeEllipsis(x)), sub(cos(protectedSqrt(sub(sin(protectedDiv(polaritySum(replaceNegatingWords(x)), hashtagPolaritySum(x))), hashtagPolaritySum(removeAllPonctuation(removeAllPonctuation(x)))))), protectedLog(emoticonsPolaritySum(removeEllipsis(removeLinks(stemmingText(removeEllipsis(removeEllipsis(x)))))))), polaritySum(removeAllPonctuation(removeLinks(removeAllPonctuation(removeStopWords(removeLinks(removeLinks(removeAllPonctuation(replaceNegatingWords(x))))))))))"
    #function_to_evaluate = "add(if_then_else(hasEmoticons(removeEllipsis(removeEllipsis(x))), sub(emoticonsPolaritySum(x), polaritySum(removeAllPonctuation(removeStopWords(replaceNegatingWords(x))))), polaritySum(stemmingText(removeEllipsis(removeStopWords(x))))), polaritySum(removeAllPonctuation(removeLinks(replaceNegatingWords(x)))))"
    #function_to_evaluate = "if_then_else(hasEmoticons(stemmingText(x)), emoticonsPolaritySum(removeEllipsis(removeStopWords(removeEllipsis(stemmingText(x))))), polaritySum(removeAllPonctuation(removeEllipsis(removeStopWords(removeAllPonctuation(removeLinks(replaceNegatingWords(removeAllPonctuation(removeLinks(removeAllPonctuation(removeEllipsis(x))))))))))))"
    #function_to_evaluate = "add(polaritySum(removeStopWords(removeEllipsis(removeAllPonctuation(removeAllPonctuation(removeLinks(removeAllPonctuation(replaceNegatingWords(removeEllipsis(removeStopWords(replaceNegatingWords(removeEllipsis(x)))))))))))), sub(mul(exp(if_then_else(True, -1.6617453540075866, -0.1240560689118353)), negativeWordsQuantity(replaceNegatingWords(removeAllPonctuation(replaceNegatingWords(x))))), negativeWordsQuantity(removeAllPonctuation(stemmingText(x)))))"
    #function_to_evaluate = "if_then_else(hasEmoticons(stemmingText(x)), emoticonsPolaritySum(removeEllipsis(removeStopWords(removeEllipsis(stemmingText(x))))), polaritySum(removeAllPonctuation(removeStopWords(replaceNegatingWords(removeEllipsis(removeEllipsis(x)))))))"
    #function_to_evaluate = "if_then_else(hasEmoticons(replaceNegatingWords(removeLinks(removeStopWords(removeLinks(x))))), emoticonsPolaritySum(x), polaritySum(removeAllPonctuation(removeAllPonctuation(removeEllipsis(removeEllipsis(removeEllipsis(replaceNegatingWords(replaceNegatingWords(removeStopWords(removeAllPonctuation(replaceNegatingWords(x))))))))))))"
    #function_to_evaluate = "polaritySum(removeAllPonctuation(removeEllipsis(removeStopWords(removeEllipsis(removeAllPonctuation(replaceNegatingWords(removeLinks(removeLinks(x)))))))))"
    #function_to_evaluate = "sub(polaritySum(replaceNegatingWords(removeAllPonctuation(removeAllPonctuation(replaceNegatingWords(removeStopWords(x)))))), sin(sin(sub(protectedDiv(negativeWordsQuantity(replaceNegatingWords(replaceNegatingWords(x))), exp(sin(hashtagPolaritySum(removeLinks(removeEllipsis(x)))))), emoticonsPolaritySum(removeStopWords(replaceNegatingWords(x)))))))"
    #function_to_evaluate = "if_then_else(hasEmoticons(x), protectedLog(invertSignal(emoticonsPolaritySum(x))), polaritySum(removeStopWords(replaceNegatingWords(removeAllPonctuation(replaceNegatingWords(replaceNegatingWords(x)))))))"

    #function_to_evaluate = "sub(add(polaritySum(replaceNegatingWords(removeStopWords(removeAllPonctuation(stemmingText(stemmingText(removeAllPonctuation(x))))))), add(add(emoticonsPolaritySum(x), emoticonsPolaritySum(x)), invertSignal(negativeWordsQuantity(removeLinks(removeLinks(removeEllipsis(removeLinks(removeStopWords(removeEllipsis(x)))))))))), invertSignal(add(polaritySum(replaceNegatingWords(removeStopWords(replaceNegatingWords(removeStopWords(replaceNegatingWords(replaceNegatingWords(replaceNegatingWords(removeStopWords(replaceNegatingWords(removeLinks(removeAllPonctuation(x)))))))))))), add(add(add(polaritySum(x), add(polaritySum(removeLinks(removeEllipsis(replaceNegatingWords(removeEllipsis(replaceNegatingWords(removeStopWords(removeEllipsis(x)))))))), add(polaritySum(replaceNegatingWords(replaceNegatingWords(removeStopWords(removeAllPonctuation(stemmingText(removeStopWords(x))))))), emoticonsPolaritySum(x)))), polaritySum(replaceNegatingWords(removeAllPonctuation(removeStopWords(replaceNegatingWords(replaceNegatingWords(replaceNegatingWords(x)))))))), polaritySum(replaceNegatingWords(removeAllPonctuation(removeStopWords(replaceNegatingWords(replaceNegatingWords(replaceNegatingWords(x)))))))))))"

    # F1 0.5994326849864792 [2067 correct evaluations] [1103 positives, 964 negatives and 0 neutrals]
    function_to_evaluate = "protectedDiv(cos(emoticonsPolaritySum(removeAllPonctuation(removeLinks(removeStopWords(stemmingText(stemmingText(removeAllPonctuation(removeLinks(x))))))))), invertSignal(if_then_else(hasEmoticons(removeStopWords(removeLinks(x))), negativeEmoticons(stemmingText(removeLinks(stemmingText(x)))), negativeWordsQuantity(removeAllPonctuation(removeAllPonctuation(removeAllPonctuation(removeAllPonctuation(removeAllPonctuation(removeAllPonctuation(removeEllipsis(x)))))))))))"


    # F1 0.6369658710978381 [2520 correct evaluations] [896 positives, 1004 negatives and 620 neutrals] on test
    #function_to_evaluate = "add(if_then_else(hasHashtag(removeAllPonctuation(removeLinks(removeStopWords(replaceNegatingWords(removeStopWords(removeStopWords(removeEllipsis(stemmingText(stemmingText(removeEllipsis(x))))))))))), 0.5759342653620698, protectedDiv(invertSignal(negativeWordsQuantity(removeAllPonctuation(removeLinks(removeEllipsis(x))))), 0.5759342653620698)), polaritySum(removeEllipsis(replaceNegatingWords(replaceNegatingWords(removeLinks(removeEllipsis(removeAllPonctuation(removeStopWords(removeLinks(x))))))))))"

    # F1 0.6232731810549077 [2444 correct evaluations] [1016 positives, 831 negatives and 597 neutrals] on test
    function_to_evaluate = "add(polaritySum(removeAllPonctuation(removeAllPonctuation(removeAllPonctuation(removeStopWords(removeAllPonctuation(replaceNegatingWords(removeAllPonctuation(removeStopWords(replaceNegatingWords(x)))))))))), sin(if_then_else(hasEmoticons(stemmingText(stemmingText(x))), if_then_else(hasEmoticons(removeAllPonctuation(x)), positiveHashtags(stemmingText(removeEllipsis(removeLinks(x)))), polaritySum(removeEllipsis(removeEllipsis(removeLinks(removeAllPonctuation(stemmingText(removeAllPonctuation(x)))))))), polaritySum(removeEllipsis(removeEllipsis(stemmingText(x)))))))"

    # F1 0.6298756475178069 [2470 correct evaluations] [1018 positives, 763 negatives and 689 neutrals] on test
    #function_to_evaluate = "add(emoticonsPolaritySum(removeLinks(removeEllipsis(stemmingText(stemmingText(removeLinks(stemmingText(removeStopWords(x)))))))), polaritySum(removeLinks(replaceNegatingWords(removeAllPonctuation(removeStopWords(replaceNegatingWords(x)))))))"


    evaluateMessages("tweets2013", function_to_evaluate)
    evaluateMessages("tweets2014", function_to_evaluate)
    evaluateMessages("sms", function_to_evaluate)
    evaluateMessages("livejournal", function_to_evaluate)
    evaluateMessages("sarcasm", function_to_evaluate)
    evaluateMessages("all", function_to_evaluate)


# log time
end = time.time()
print("\n\n[Script ends after " + str(format(end - start, '.3g')) + " seconds]")