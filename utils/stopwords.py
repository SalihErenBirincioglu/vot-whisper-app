#stopword list
STOPWORDS = {
    # bağlaçlar
    "ve", "veya", "ama", "fakat", "ancak", "çünkü", "ya", "ya da",

    # zamirler
    "ben", "sen", "o", "biz", "siz", "onlar",
    "bana", "sana", "ona", "bizi", "sizi", "onları",

    # işaret / belirsizlik
    "bu", "şu", "o", "bunlar", "şunlar",
    "her", "hiç", "bazı", "çok", "az",

    # ek-fiil ve yardımcılar
    "idi", "imiş", "ise", "mi", "mı", "mu", "mü",
    "de", "da", "ki",

    # zaman / dolgu
    "şimdi", "sonra", "önce", "artık",
    "bugün", "yarın", "dün",

    # konuşma dili (Whisper çok üretir)
    "yani", "işte", "şey", "falan", "filan", "hani"
}