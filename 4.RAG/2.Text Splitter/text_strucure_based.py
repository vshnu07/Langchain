from langchain_text_splitters import RecursiveCharacterTextSplitter

text="""
Cricket: A Sport of Passion and Teamwork

Cricket is one of the most popular sports in the world, especially in countries like India, Australia, England, Pakistan, South Africa, and Sri Lanka. It is a game played between two teams, with each team consisting of eleven players. Cricket is not just a sport; it is a combination of teamwork, discipline, patience, strategy, and dedication. Millions of people enjoy watching and playing cricket, making it an important part of sporting culture across the world.

The history of cricket dates back several centuries to England, where it developed as a traditional outdoor game. Over time, it became an internationally recognized sport and spread to different countries. Today, cricket is played in three major international formats: Test matches, One Day Internationals, and Twenty20. Each format has its own rules, strategies, and challenges. Test cricket is played over five days and tests the patience and technical abilities of players. One Day International matches consist of fifty overs per team, while T20 matches consist of twenty overs per team and focus on aggressive batting and fast-paced entertainment.

A cricket team consists of different types of players, including batters, bowlers, all-rounders, and wicketkeepers. Batters are responsible for scoring runs by hitting the ball and running between the wickets or hitting boundaries. Bowlers attempt to dismiss batters by delivering the ball strategically. All-rounders contribute through both batting and bowling, while wicketkeepers play an important role behind the stumps. Every player has a specific responsibility, and the performance of the entire team depends on cooperation and coordination.

India has a special connection with cricket. It is followed by millions of fans, and international matches create excitement throughout the country. Many young children dream of becoming professional cricketers and representing India at the international level. Legendary Indian players such as Sachin Tendulkar, MS Dhoni, Virat Kohli, Rohit Sharma, and Rahul Dravid have inspired generations through their performances and achievements. Their dedication, hard work, and consistency demonstrate what can be achieved through determination.

The Indian Premier League, commonly known as the IPL, has played a significant role in making cricket more popular. It brings together talented players from different countries and provides opportunities for young cricketers to showcase their abilities. The tournament is known for its exciting matches, competitive teams, powerful batting performances, and dramatic finishes.

Modern cricket has also benefited from technological developments. Technologies such as the Decision Review System, ball-tracking systems, and video replays help umpires make more accurate decisions. Fitness training, data analysis, and modern coaching techniques have improved the overall performance of professional players.

Cricket teaches several valuable life lessons. It develops discipline, patience, leadership, communication, and teamwork. Players learn how to handle pressure, accept defeat, celebrate success, and support one another. These qualities are useful not only in sports but also in education and professional careers.

In conclusion, cricket is much more than a game played with a bat and a ball. It brings people together, creates unforgettable memories, and inspires millions of individuals. Whether it is played on a professional stadium, a school playground, or a small street, cricket continues to spread happiness, friendship, and sportsmanship across the world.
"""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
    separators=''
)

result=splitter.split_text(text)
print(len(result))
print(result)
