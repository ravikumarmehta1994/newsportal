from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,"testapp/home.html")
def Movies_news(request):
    news1="Kareena Kapoor says biggest taboo for female actors was to get married "
    news2="Can RRR's 'Naatu Naatu' make history and bring home an Oscar for India? "
    news3="Oscar 2023 predictions: Who will win best actor, best actress and best film awards"
    news4="Satish Kaushik death: Delhi Police waiting for postmortem report of actor, yet to confirm cause of death"
    dic_1={'n1':news1,'n2':news2,'n3':news3,'n4':news4}
    return render(request,'testapp/movies.html',dic_1)
def sports_news(request):
    news5="IND vs AUS Live Score, 4th Test: India post 129/1 at Lunch vs Australia"
    news6="Watch: Gautam Gambhir, Shahid Afridi's brief exchange sparks old rivalry, highly awkward handshake triggers meme fest"
    news7="Rohit Sharma joins Tendulkar, Kohli, Dravid in enormous batting record; becomes only sixth Indian to reach feat"
    news8="'He runs like a rat going after cheese but the difference is...': Karthik's bizarre analogy involving Sachin Tendulkar"
    dic_2={'n5':news5,"n6":news6,'n7':news7,'n8':news8}
    return render(request,'testapp/sports.html',dic_2)
def polity_news(request):
    news9="India-Australia talk: Both PMs agree to take collective action against terrorism"
    news10="Pakistan skips Shanghai Cooperation Organisation chief justice meet hosted by India"
    news11="KCR's daughter K Kavitha at ED office in Delhi for questioning: 10 points"
    news12="Morning brief: Juvenile among 4 held for harassing Japanese woman on Holi in Delhi; all the latest news"
    dic_3={'n9':news9,"n10":news10,'n11':news11,'n12':news12}
    return render(request,'testapp/polity.html',dic_3)