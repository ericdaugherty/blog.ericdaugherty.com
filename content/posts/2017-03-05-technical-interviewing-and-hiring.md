---
title: "Technical Interviewing and Hiring"
date: 2017-03-05T02:35:00.003Z
url: /2017/03/technical-interviewing-and-hiring.html
draft: false
---
There has been some discussion in the technical community recently about the use of algorithms and coding tests during the interview process. &nbsp;Here is a sample:

<blockquote class="twitter-tweet" data-lang="en">
<div dir="ltr" lang="en">
Hello, my name is David. I would fail to write bubble sort on a whiteboard. I look code up on the internet all the time. I don't do riddles.</div>
— DHH (@dhh) <a href="https://twitter.com/dhh/status/834146806594433025">February 21, 2017</a></blockquote>
<script async="" charset="utf-8" src="//platform.twitter.com/widgets.js"></script>

<blockquote class="twitter-tweet" data-lang="en">
<div dir="ltr" lang="en">
Hi, I'm Py. Used to think I didn't need to learn CS. I was lazy. I practiced for interviews, and it made me a better Software Engineer. <a href="https://t.co/yD5NzcmTwF">https://t.co/yD5NzcmTwF</a></div>
— Py ⚔ (@Piwai) <a href="https://twitter.com/Piwai/status/834817808940756992">February 23, 2017</a></blockquote>
I have my own thoughts I would like to share, but this isn't really a topic for 140 characters.

<h3>
Why should you care what I think?</h3>
I've spent a lot of time interviewing and hiring developers across several organizations. For a while I was doing interviews every day. In fact, I remember telling my recruiter that he couldn't schedule more than 2 interviews in a day because by the third interview I found I was no longer effective. I estimate that I've interviewed over 300 candidates, and been the primary decision maker on over half of those. &nbsp;I have been a key member of the interviewing and/or hiring team in two custom software services companies that have grown from 30 or fewer people to over 115 during my tenure. &nbsp;I've done this a lot, and I was there to see my successes and my failures.

<!--more-->

I spent over a decade primarily as a software developer. I've written production code in LabView, C++,&nbsp;J++,&nbsp;Java, VB, Perl, C#/.Net, JavaScript, Flex, Scala, Objective-C, and probably more. I've probably written more Java than the rest combined, but I was always learning something new and during the time that I was doing these interviews, I knew what I was talking about. I would like to think I still very technically competent, although many of my current employees enjoy proving me wrong regularly.

I leaned this approach from a great mentor early on, and adopted and extended it over the years. We all stand on the shoulders of giants.

<h3>
Is this the one true way?</h3>
Before I describe my approach, I want to focus on a key point lost among the 140 character conversations. &nbsp;Your interview process should identify candidates that will work in YOUR organization. Your company probably isn't just like David Heinemeier Hansson's, or anyone else you read on twitter. &nbsp;It probably isn't just like the companies I've worked for either, so if you blindly copy what was successful for me, you will probably still fail.

I've spent most of my career working for services companies building great software, from enterprise back-end systems in Java and .Net to amazing mobile applications in Objective-C, Swift, Java, and Kotlin. Because these companies are services companies, I expect my employees to be able to interact directly with out clients. The people I hire must be capable of more than just writing great code, they must solve our clients problems, by understanding what they really need, communicating effectively with technical and non-technical people alike, and delivering a great technical solutions.

I also expect my employees to be able to learn a new technology quickly. The landscape is always changing, and when you are building software for other companies, you do not have the luxury to define what technologies are and are not acceptable.

Therefore, I focus on hiring great problem solvers. If you are not a good problem solver, you will not work on my teams, no matter how amazing you are at language/framework/platform XYZ.

<h3>
So what is the interview like?</h3>
<div>
Most of these interviews last about an hour. The four sections are...</div>
<h4>
Cool Stuff - ~15 Minutes</h4>
<div>
I start all the interviews by asking the candidate what projects they think are cool or projects they are proud of. These can be work projects, open-source projects, school projects, or just tinkering around and learning projects. This engages the candidate and allows them to talk about topics they are comfortable with.</div>
<div>

</div>
<div>
This tells me several things. First, it tells me whether they communicate effectively. I actually prefer when they have a project in an area that I am not knowledgeable. Selfishly, it lets me learn about something new, but the primary reason is that it show me whether they can explain a technical concept to me that they understand well. If it is in an area that I know well, it lets me probe to see how well they really understand the topic.</div>
<div>

</div>
<div>
It also helps me level-set where the candidate is. Ignoring their resume, the projects and accomplishments they are proud of tell a very clear story about their skill level and world view.</div>
<h4>
Coding Problems - ~20 Minutes</h4>
<div>
What!?! Yes, I have two basic coding/problem solving problems that I make each candidate work through, on paper, in front of me.</div>
<div>

</div>
<div>
<b>Problem 1:</b></div>
<div>
This is essentially a recursive coding problem. You can solve it in any OO programing language with a basic knowledge of the core syntax. It does not require any API/Framework specific knowledge. The right answer is about 4 lines of code.</div>
<div>

</div>
<div>
I have given this problem to everyone from college students looking for their first job to senior architects. They should all be able to solve it. I do adjust my expectations based on the level indicated by their resume and 'Cool Stuff' answers.</div>
<div>

</div>
<div>
Achieving a Passing mark on this doesn't necessarily require a perfect answer right away. I'm happy to ask questions, and give small hints to the candidates if they get stuck. This is actually one of the most valuable parts of the process because it allows me to see how well they listen, and how they think through a problem. But if you can't write (simple) code down on paper with a reasonable level of accuracy, and you can't write a basic recursive method with a few hints, you are probably not going to cut it.</div>
<div>

</div>
<div>
<b>Problem 2:</b></div>
<div>
This is where I date myself somewhat. &nbsp;Problem #2 is ideally writing a SQL statement, but is really a boolean logic problem. It does not require anything other than very basic SQL syntax. &nbsp;No Joins, or anything even slightly fancy. The right answer would fit in a single tweet.</div>
<div>

</div>
<div>
Again, I have given this problem to everyone from college students looking for their first job to senior architects.&nbsp;They should all be able to solve it. I have run into college students that didn't know SQL, and in those cases I was able to adapt it to be a boolean logic problem that they could solve in general set notation.</div>
<div>

</div>
<div>
Again, success here is showing me how you think through and solve problems. You don't need to write the correct answer down flawlessly the first time, but you have to show me that you can think through a problem, listen to feedback/hints if necessary and incorporate them into your thinking.</div>
<div>

</div>
<div>
<b>Alternate Problem:</b></div>
<div>
Depending on time and level, another question I've asked A LOT, mostly to Java and .Net candidates, is how garbage collection works in the JVM (or on .Net).</div>
<div>

</div>
<div>
Occasionally I'll get a candidate that actually knows the answer, and while impressive, this is actually somewhat disappointing. &nbsp;The point of this question is to have them show me their problem solving skills applied to a real technology that they depend on every day, but probably don't think about.</div>
<div>

</div>
<div>
This questions shows me how well a candidate can listen, how well do they think on their feet, and how well do they actually understand computer science concepts.</div>
<div>

</div>
<div>
Again, the 'right answer' isn't necessarily the point. Having a great conversation with me where in the end they really grasp the concept and feel like they are a better developer makes both me and the candidate feel good about the interview.</div>
<div>

</div>
<div>
<b>Side Note:</b> I was working with a startup (not my full time job) and helping them make their first full time developer hire. I used these problems and rejected a candidate. The CTO, who had not actively developed in several years, challenged me about the questions, so I gave him the interview. He passed both in less than 10 minutes, and realized that he didn't want anyone on his team that couldn't solve these problems. The next person we interviewed passed, was hired, and did a great job for them for several years.</div>
<h4>
Resume Due Diligence ~ 15 Minutes</h4>
<div>
Once the problems are solved, I will use the next section to tackle any areas of interest that I think are appropriate. I will often read through the resume and ask questions about specific projects/accomplishments to determine how accurate the descriptions are and what role the candidate actually had on those projects.</div>
<div>

</div>
<div>
If they profess deep knowledge in a certain language/framework/platform, I may go deep in this area to see how much of an expert they really are. I love learning something new from&nbsp;candidates, and they usually enjoy teaching the interviewer something new as well!</div>
<div>

</div>
<div>
A big take-away from this section is: how honest are they about their resume? Were they exaggerating, or underselling themselves?</div>
<div>

</div>
<div>
I can also use this time to follow up on areas the candidate showed a particular interest in to see how deep their knowledge is.</div>
<h4>
Candidate Questions ~ 10 Minutes</h4>
<div>
The final section is an opportunity for the candidate to ask me questions, about the role, culture, expectations, etc. While this is a key part in making sure the candidate is sold on working for me, their questions are also a window into their thought process and outlook, and can be informative in making a hire/no-hire decision.</div>
<div>

Ultimately thought, this section is about closing the candidate. Regardless of whether you will hire the candidate, you want them to be sold on your company, and you want them to feel good about the experience. Even if you pass on them, you want them to leave the interview with a positive opinion of you and your company. <b>It is a small world.</b></div>
<h3>
Why do I do is this way?</h3>
<div>
I've covered a lot of the why along the way, but it important to reiterate and expand on my motivations and goals.</div>
<div>

</div>
<div>
First, I want to reiterate that I target hiring great technical consultants. We build software solutions for other companies, and the skills we look for reflect that. This is probably not a great approach for other types of companies.</div>
<div>

</div>
<div>
I firmly believe that in order to be a great software consultant, you have to be a great problem solver. To me, this includes listening and understanding the problem (solving the right problem), deep enough technical expertise to identify a good solution (there is rarely one RIGHT solution), the ability to communicate what the solution is, what the trade-offs are (there are always trade-offs) and how it addresses the actual problem, and the ability to deliver the solution.</div>
<div>

</div>
<div>
In the companies that I worked for, we certainly didn't expect an Associate Developer to interact directly with the client and execute all of these steps, but this is still the ultimate process and everyone should be able to participate at the level of their experience.</div>
<div>

</div>
<div>
I also don't believe in team interviewing for smaller services companies. A consultant working for one of these companies will need to be successful across different clients and different teams. I believe in the accountability of a single decision maker, and if the process is consistent, then the team members know the people getting hired went through the same process they did. Ultimately, if the team trusts the hiring manager, they will trust the candidate that they hire. However, this doesn't scale and as a company grows, the process needs to evolve.</div>
<div>

</div>
<div>
Again, this probably doesn't work for other types of companies, and team interviews make sense in a lot of cases.</div>
<div>

</div>
<div>
Finally, I do it this way because it works. Yes, I made a few bad hires over the years. In each case, I went back to look at the interview notes to see what I missed and how I could do better next time. In some cases I was being too optimistic because I was desperate to fill a need. In some cases the candidate simply snowed me. In some cases, there is an issue that I can't reasonably expect to uncover in an interview.</div>
<h4>
Final Notes</h4>
<div>
The lifeblood of the interview/hiring process is the great work that your recruiters do. I firmly believe in having in house recruiters and I've been blessed to work with some great ones. You know who you are, thank you.</div>
<div>

</div>
<div>
I have no idea how many false negatives I've had. I would argue it is unknowable. But the growth of both companies would suggest that I didn't turn away too many qualified candidates.</div>
<div>

</div>
<div>
These opinions are my own, and do not reflect those of my employer. I am no longer in a role where I make any hiring decisions on technical candidates, so don't expect that reading this post will give you an inside edge. ;)</div>
<div>

</div>
<div>
This post is too long. Unfortunately, I'm not a good enough writer to write a shorter post. &nbsp;I'm sorry.</div>
<script async="" charset="utf-8" src="//platform.twitter.com/widgets.js"></script>
