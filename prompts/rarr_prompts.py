"""All prompts used for RARR prompting."""

QGEN_PROMPT = """I will check things you said and ask questions.

You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This is to prevent a buildup of mucus. It’s called the nasal cycle.
To verify it,
1. I googled: Does your nose switch between nostrils?
2. I googled: How often does your nostrils switch?
3. I googled: Why does your nostril switch?
4. I googled: What is nasal cycle?

You said: The Stanford Prison Experiment was conducted in the basement of Encina Hall, Stanford’s psychology building.
To verify it,
1. I googled: Where was Stanford Prison Experiment was conducted?

You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency list. It is named after Vaclav Havel and Samih Hakimi.
To verify it,
1. I googled: What does Havel-Hakimi algorithm do?
2. I googled: Who are Havel-Hakimi algorithm named after?

You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.
To verify it,
1. I googled: Who sings the song "Time of My Life"?
2. I googled: Which film is the song "Time of My Life" from?
3. I googled: Who produced the song "Time of My Life"?

You said: Kelvin Hopins was suspended from the Labor Party due to his membership in the Conservative Party.
To verify it,
1. I googled: Why was Kelvin Hopins suspended from Labor Party?

You said: Social work is a profession that is based in the philosophical tradition of humanism. It is an intellectual discipline that has its roots in the 1800s.
To verify it,
1. I googled: What philosophical tradition is social work based on?
2. I googled: What year does social work have its root in?

You said: {claim}
To verify it,
""".strip()

AGREEMENT_GATE_PROMPT = """I will check some things you said.

1. You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This is to prevent a buildup of mucus. It’s called the nasal cycle.
2. I checked: How often do your nostrils switch?
3. I found this article: Although we don’t usually notice it, during the nasal cycle one nostril becomes congested and thus contributes less to airflow, while the other becomes decongested. On average, the congestion pattern switches about every 2 hours, according to a small 2016 study published in the journal PLOS One.
4. Reasoning: The article said the nose’s switching time is about every 2 hours, and you said the nose's switching time is about every 45 minutes.
5. Therefore: This disagrees with what you said.

1. You said: The Little House books were written by Laura Ingalls Wilder. The books were published by HarperCollins.
2. I checked: Who published the Little House books?
3. I found this article: These are the books that started it all -- the stories that captured the hearts and imaginations of children and young adults worldwide. Written by Laura Ingalls Wilder and published by HarperCollins, these beloved books remain a favorite to this day.
4. Reasoning: The article said the Little House books were published by HarperCollins and you said the books were published by HarperCollins.
5. Therefore: This agrees with what you said.

1. You said: Real Chance of Love was an American reality TV show. Season 2 of the show was won by Cali, who chose to be with Chance.
2. I checked: Who won season 2 of Real Chance of Love?
3. I found this article: Real Chance of Love 2: Back in the Saddle is the second season of the VH1 reality television dating series Real Chance of Love. Ahmad Givens (Real) and Kamal Givens (Chance), former contestants on I Love New York are the central figures.
4. Reasoning: The article doesn't answer the question and you said that Cali won season 2 of Real Chance of Love.
5. Therefore: This is irrelevant to what you said.

1. You said: The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building.
2. I checked: Where was Stanford Prison Experiment conducted?
3. I found this article: Carried out August 15-21, 1971 in the basement of Jordan Hall, the Stanford Prison Experiment set out to examine the psychological effects of authority and powerlessness in a prison environment.
4. Reasoning: The article said the Stanford Prison Experiment was conducted in Jordan Hall and you said the Stanford Prison Experiment was conducted in Jordan Hall.
5. Therefore: This agrees with what you said.

1. You said: Social work is a profession that is based in the philosophical tradition of humanism. It is an intellectual discipline that has its roots in the 1800s.
2. I checked: When did social work have its roots?
3. I found this article: The Emergence and Growth of the Social work Profession. Social work’s roots were planted in the 1880s, when charity organization societies (COS) were created to organize municipal voluntary relief associations and settlement houses were established.
4. Reasoning: The article said social work has its roots planted in the 1880s and you said social work has its root in the 1800s.
5. Therefore: This disagrees with what you said.

1. You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency list. It is named after Vaclav Havel and Samih Hakimi.
2. I checked: What is the Havel-Hakimi algorithm?
3. I found this article: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. This construction is based on a recursive algorithm. The algorithm was published by Havel (1955), and later by Hakimi (1962).
4. Reasoning: The article said the Havel-Hakimi algorithm is for constructing a special solution if a simple graph for the given degree sequence exists and you said the Havel-Hakimi algorithm is for converting the adjacency matrix of a graph.
5. Therefore: This disagrees with what you said.

1. You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.
2. I checked: Who was the producer of "(I’ve Had) The Time of My Life"?
3. I found this article: On September 8, 2010, the original demo of this song, along with a remix by producer Michael Lloyd , was released as digital files in an effort to raise money for the Patrick Swayze Pancreas Cancer Resarch Foundation at Stanford University.
4. Reasoning: The article said that a demo was produced by Michael Lloyd and you said "Time of My Life" was produced by Michael Lloyd.
5. Therefore: This agrees with what you said.

1. You said: Tiger Woods is the only player who has won the most green jackets. He has won four times. The Green Jacket is one of the most coveted prizes in all of golf.
2. I checked: What is the Green Jacket in golf?
3. I found this article: The green jacket is a classic, three-button, single-breasted and single-vent, featuring the Augusta National Golf Club logo on the left chest pocket. The logo also appears on the brass buttons.
4. Reasoning: The article said the Green Jacket is a classic three-button single-breasted and single-vent and you said the Green Jacket is one of the most coveted prizes in all of golf.
5. Therefore: This is irrelevant to what you said.

1. You said: Kelvin Hopins was suspended from the Labor Party because he had allegedly sexually harassed and behaved inappropriately towards a Labour Party activist, Ava Etemadzadeh.
2. I checked: Why was Kelvin Hopins suspeneded from the Labor Party?
3. I found this article: A former Labour MP has left the party before an inquiry into sexual harassment allegations against him was able to be concluded, the party has confirmed. Kelvin Hopkins was accused in 2017 of inappropriate physical contact and was suspended by the Labour party pending an investigation.
4. Reasoning: The article said Kelvin Hopins was suspended because of inappropriate physical contact and you said that Kelvin Hopins was suspended because he allegedly sexually harassed Ava Etemadzadeh.
5. Therefore: This agrees with what you said.

1. You said: In the battles of Lexington and Concord, the British side was led by General Thomas Smith.
2. I checked: Who led the British side in the battle of Lexington and Concord?
3. I found this article: Interesting Facts about the Battles of Lexington and Concord. The British were led by Lieutenant Colonel Francis Smith. There were 700 British regulars.
4. Reasoning: The article said the British side was led by Lieutenant Colonel Francis Smith and you said the British side was led by General Thomas Smith.
5. Therefore: This disagrees with what you said.

1. You said: {claim}
2. I checked: {query}
3. I found this article: {evidence}
4. Reasoning:
""".strip()

EDITOR_PROMPT = """I will fix some things you said.

1. You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This is to prevent a buildup of mucus. It’s called the nasal cycle.
2. I checked: How often do your nostrils switch?
3. I found this article: Although we don’t usually notice it, during the nasal cycle one nostril becomes congested and thus contributes less to airflow, while the other becomes decongested. On average, the congestion pattern switches about every 2 hours, according to a small 2016 study published in the journal PLOS One.
4. This suggests 45 minutes switch time in your statement is wrong.
5. My fix: Your nose switches back and forth between nostrils. When you sleep, you switch about every 2 hours. This is to prevent a buildup of mucus. It’s called the nasal cycle.

1. You said: In the battles of Lexington and Concord, the British side was led by General Thomas Hall.
2. I checked: Who led the British side in the battle of Lexington and Concord?
3. I found this article: Interesting Facts about the Battles of Lexington and Concord. The British were led by Lieutenant Colonel Francis Smith. There were 700 British regulars.
4. This suggests General Thomas Hall in your statement is wrong.
5. My fix: In the battles of Lexington and Concord, the British side was led by Lieutenant Colonel Francis Smith.

1. You said: The Stanford Prison Experiment was conducted in the basement of Encina Hall, Stanford’s psychology building.
2. I checked: Where was Stanford Prison Experiment conducted?
3. I found this article: Carried out August 15-21, 1971 in the basement of Jordan Hall, the Stanford Prison Experiment set out to examine the psychological effects of authority and powerlessness in a prison environment.
4. This suggests Encina Hall in your statement is wrong.
5. My fix: The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building.

1. You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency list. It is named after Vaclav Havel and Samih Hakimi.
2. I checked: What is the Havel-Hakimi algorithm?
3. I found this article: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. This construction is based on a recursive algorithm. The algorithm was published by Havel (1955), and later by Hakimi (1962).
4. This suggests the Havel-Hakimi algorithm’s functionality in your statement is wrong.
5. My fix: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. It is named after Vaclav Havel and Samih Hakimi.

1. You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Phil Ramone.
2. I checked: Who was the producer of "(I’ve Had) The Time of My Life"?
3. I found this article: On September 8, 2010, the original demo of this song, along with a remix by producer Michael Lloyd , was released as digital files in an effort to raise money for the Patrick Swayze Pancreas Cancer Resarch Foundation at Stanford University.
4. This suggests "Time of My Life" producer name in your statement is wrong.
5. My fix: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.

1. You said: Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels with approximately 1.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited.
2. I checked: What is the area of Phoenix Market City in Pune?
3. I found this article: Phoenix Market City was opened in January 2013 and has the distinction of being the largest mall in the city of Pune, with the area of 3.4 million square feet. It is located in the Viman Nagar area of Pune.
4. This suggests the 1.4 million square feet of built-up space in your statment is wrong.
5. My fix: Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels with approximately 3.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited.

1. You said: {claim}
2. I checked: {query}
3. I found this article: {evidence}
4. This suggests
""".strip()
