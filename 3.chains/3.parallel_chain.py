from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

from dotenv import load_dotenv

load_dotenv()

prompt1=PromptTemplate(
    template="Genearate a simple and short notes from the text \n {text}",
    input_variables=["text"]
)

prompt2=PromptTemplate(
    template="Generate around 5 to 10 mcq questions from the following text \n {text}",
    input_variables=["text"]
)

prompt3=PromptTemplate(
    template="combine notes and mcq questions into a single document \n  notes->{notes} and quiz->{quiz}",
    input_variables=["notes","quiz"]
)

model=ChatOllama(model="llama3.2:latest")

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    "notes":prompt1 | model | parser,
    "quiz": prompt2 | model | parser
})

merge_chain= prompt3 | model | parser

chain=parallel_chain | merge_chain

text="""
Virat Kohli is one of the most prominent cricketers of the modern era and has played a major role in Indian cricket. Born on November 5, 1988, in Delhi, India, Kohli developed an interest in cricket at a young age. His talent and dedication became evident during his early years, and he eventually joined the West Delhi Cricket Academy to receive professional training. His journey from a young cricket enthusiast in Delhi to becoming one of India's most successful international batsmen is often associated with discipline, determination, and consistency.

Kohli gained significant attention when he captained the Indian Under-19 cricket team to victory in the 2008 ICC Under-19 Cricket World Cup. His performances at the junior level helped him earn opportunities at the senior level, and he made his international debut for India in 2008. During the early stages of his international career, Kohli had to compete for a permanent position in a strong Indian batting lineup. Over time, consistent performances helped him establish himself as an important member of the team.

One of Kohli's greatest strengths has been his ability to score runs across different formats of cricket. In One Day Internationals, he became particularly well known for his performances while chasing targets. His ability to manage pressure, rotate the strike, find boundaries, and accelerate when required made him a highly effective batsman in limited-overs cricket. His consistency resulted in numerous centuries and match-winning performances for India.

In Test cricket, Kohli developed into an aggressive and technically accomplished batsman capable of performing in different conditions around the world. Playing Test cricket in countries such as Australia, England, South Africa, and New Zealand requires players to adapt to different pitches, weather conditions, and bowling attacks. Kohli worked extensively on his technique and fitness to compete successfully in challenging overseas environments.

Kohli also became an important leader for the Indian cricket team. After taking on major captaincy responsibilities, he encouraged an aggressive and competitive style of cricket. Fitness became a particularly important part of the team's culture during his leadership period. Kohli himself became known for maintaining high fitness standards, and his approach influenced many younger Indian cricketers to focus more seriously on strength, conditioning, nutrition, and athleticism.

Under Kohli's Test leadership, India achieved considerable success and developed a strong group of fast bowlers capable of competing in overseas conditions. His leadership style was energetic and expressive, and he frequently demonstrated his emotions on the field. While his aggressive approach sometimes generated debate among cricket fans and commentators, it also became an important part of his identity as a player and captain.

Kohli has also had a major presence in the Indian Premier League. He has been strongly associated with Royal Challengers Bengaluru throughout his IPL career. His performances for the franchise have included several memorable seasons and innings. His connection with the franchise and its supporters has made him one of the most recognizable players in the history of the tournament.

Another significant aspect of Kohli's career is his approach to fitness. During the earlier part of his career, he made major changes to his diet, training, and lifestyle. He has frequently discussed the importance of discipline and physical preparation in professional sport. His transformation demonstrated how improvements outside traditional cricket practice could contribute to performance on the field.

Like most professional athletes, Kohli has experienced periods when his performances did not meet the extremely high expectations surrounding him. At various stages of his career, he faced criticism when centuries and major scores became less frequent. Because he had established such high standards, even relatively normal periods without major scores attracted significant attention. Kohli continued playing through these difficult periods and eventually returned to producing important performances.

His batting style combines technical ability with intensity. One of his most recognizable shots is the cover drive, where the ball is struck through the off-side with timing and placement. He is also known for running aggressively between the wickets. Instead of depending entirely on boundaries, Kohli frequently converts singles into doubles and maintains pressure on fielding teams through quick running.

Kohli's influence extends beyond cricket. He has become one of India's most recognizable sports personalities and has been associated with numerous brands and commercial ventures. His large following on social media has also allowed him to communicate directly with millions of supporters around the world. This level of popularity demonstrates how modern athletes can become global public figures beyond their performances in sport.

Despite his achievements, Kohli's career has also included challenges, criticism, defeats, changes in leadership responsibilities, and fluctuations in form. These experiences are an important part of understanding his career because professional sport involves both success and failure. His ability to continue competing after difficult periods has contributed to his reputation for determination.

Kohli has played alongside multiple generations of Indian cricketers and has been part of India's transition from the era of players such as Sachin Tendulkar, Virender Sehwag, and MS Dhoni to a newer generation of players. During this transition, Kohli developed from a young batsman into a senior member of the team and eventually became an influential figure for younger players.

His career also illustrates how cricket has evolved in the modern era. Contemporary international cricketers often have to move between Test matches, One Day Internationals, T20 cricket, franchise tournaments, extensive travel schedules, training sessions, media commitments, and commercial responsibilities. Performing consistently across these environments requires technical ability as well as physical and mental preparation.

Virat Kohli's legacy in cricket is closely connected to his run-scoring, competitiveness, fitness standards, leadership, and ability to perform under pressure. His career has inspired many young players who admire his intensity and dedication to the sport. Regardless of comparisons with other great batsmen, his contribution to Indian cricket and his influence on the modern game have made him one of the defining cricketers of his generation.
"""

result=chain.invoke({"text":text})
print(result)