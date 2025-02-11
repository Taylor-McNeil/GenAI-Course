# AI Sentence Constructor Exploration 🚀

## Purpose of this Exercise 
To understand the risks, complications, and explore the potential for adding an AI-driven sentence constructor to our current website offerings. We are currently serving **1,000 students worldwide**, teaching them **Japanese**. This exploration aims to determine if adding this feature would be **feasible and valuable**.


## Requirements 📋

### Business Requirements 💼
- This new feature should attract **at least 100 new students**.
- It should **improve student retention and learning**.
- Success is measured by tracking **student scores** before and after the introduction of the sentence constructor feature.

### Functional Requirements 🛠️
- The feature must **help students translate sentences** from **English to Japanese** without directly giving them the answer.
- It should act as a **tutor**, providing **tips and hints** to guide students toward the correct translation.
- The tutor should give **examples in Kanji and English** to support student comprehension.



## Risks & Mitigation Strategies ⚠️

### Risks
1. **Costs** 💰 - Running LLMs can be expensive.
2. **Exposure to incorrect information** ❌ - AI models may generate inaccurate translations.
3. **LLM availability** 🔄 - Downtime or external dependency on third-party models.
4. **Potential misuse of the flagging system** 🚩 - Students may abuse the system to earn rewards or flag correct responses as incorrect.

### Mitigation Strategies 
- **Cost Control:** Use **free LLMs** where possible and **implement rate limits** to prevent overuse.
- **LLM Availability:**
  - Explore **self-hosting** a downloadable model to reduce reliance on external services.
  - Implement **fallback mechanisms**, such as a **cloud-based API** during peak usage times or unexpected model failures.
- **Accuracy Improvement:**
  - Implement a **flagging system** where students can report incorrect answers.
  - Teachers can review flagged responses.
  - Reward students who correctly flag wrong answers.
  - Introduce **safeguards** to prevent misuse of the flagging system, such as:
    - Limits on how many flags a student can submit in a given time frame to prevent misuse.
  - Store flagged wrong answers in a **cache** to improve model learning and avoid repeated mistakes.



## Next Steps 
- Evaluate the feasibility of **hosting our own model**.
- Define a **testing period** to measure student improvement.
- Develop a **prototype** and conduct trials with a subset of students.

---
