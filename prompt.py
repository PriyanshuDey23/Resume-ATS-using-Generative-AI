PROMPT1="""
"Analyze the resume I've uploaded as an image and provide a summary of the following information:
- Contact information
- Education background
- Work experience (including job titles, company names, and dates)
- Key skills and certifications
- Any relevant achievements or awards
Also, suggest:
- Any missing sections or information that would strengthen the resume
- Potential job titles or industries aligned with the experience and skills listed
- Recommendations for improvement in formatting, clarity, or content
Please provide your analysis in a clear and concise format."
"""


PROMPT2="""
Based on the resume I've uploaded as an image and the job description provided below, identify the key requirements and suggest ways for me to improve my skills and qualifications to better match the job requirements.
Job Description:
{input_text}
Please provide:
- A gap analysis: Identify the skills and qualifications mentioned in the job description that are missing or underdeveloped in my resume.
- Personalized improvement plan: Recommend specific courses, certifications, training programs, or experiences that would help bridge the gaps.
- Skill enhancement suggestions: Provide actionable advice on how to develop and showcase relevant skills, including projects, volunteer work, or other activities.
- Relevant keywords: Highlight key phrases and terms from the job description that I should incorporate into my resume and cover letter.
Format your response as follows:

Gap Analysis
[List missing/underdeveloped skills]

Improvement Plan
[Recommendations for courses, certifications, etc.]

Skill Enhancement
[Actionable advice for skill development]

Keyword Integration
[List relevant keywords for resume/cover letter]

Please provide your analysis and suggestions in a clear and concise format.
"""


PROMPT3="""
Analyze the resume I've uploaded as an image and the job description provided below, then identify the missing keywords and phrases that are crucial for the job.

Job Description:
{input_text}

Please:
- Extract relevant keywords and phrases from the job description.
- Compare them with the content of my uploaded resume.
- Identify the missing keywords and phrases that are:
1.Frequently mentioned in the job description
2.Highly relevant to the job requirements
3.Absent or underrepresented in my resume

Provide the results in two sections:

Missing Keywords
[List keywords/phrases missing from resume, prioritized by frequency/relevance]

Integration Suggestions
[Recommendations on how to naturally incorporate missing keywords into:
- Resume summary/objective
- Work experience descriptions
- Skills section
- Education/certifications

Also, indicate:
- Frequency count: How many times each missing keyword appears in the job description
- Relevance score: A score (e.g., 1-5) indicating how crucial each missing keyword is to the job requirements

Format your response for easy reference.
"""

PROMPT4= """
Calculate the percentage match between my uploaded resume (image) and the provided job description.

Job Description:
{input_text}

Assess the alignment between my resume and the job requirements based on:
- Keyword overlap
- Skill relevance
- Education and certification matches
- Work experience alignment

Provide the results in the following format:
- Match Percentage: [XX%]

Breakdown:
- Keyword Match: [XX%]
- Skill Relevance: [XX%]
- Education/Certification Match: [XX%]
- Work Experience Alignment: [XX%]
"""