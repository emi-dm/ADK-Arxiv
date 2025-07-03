# Research Papers Collection

Generated on: 2025-07-03 12:14:31

---

## 1. Model Context Protocol (MCP) at First Glance: Studying the Security and Maintainability of MCP Servers

**Authors:** Mohammed Mehedi Hasan, Hao Li, Emad Fallahzadeh, Gopi Krishnan Rajbahadur, Bram Adams, Ahmed E. Hassan

**Published:** 2025-06-16

**Categories:** 

**URL:** [http://arxiv.org/pdf/2506.13538v4](http://arxiv.org/pdf/2506.13538v4)

**Abstract:**
Although Foundation Models (FMs), such as GPT-4, are increasingly used in
domains like finance and software engineering, reliance on textual interfaces
limits these models' real-world interaction. To address this, FM providers
introduced tool calling-triggering a proliferation of frameworks with distinct
tool interfaces. In late 2024, Anthropic introduced the Model Context Protocol
(MCP) to standardize this tool ecosystem, which has become the de facto
standard with over eight million weekly SDK downloads. Despite its adoption,
MCP's AI-driven, non-deterministic control flow introduces new risks to
sustainability, security, and maintainability, warranting closer examination.
  Towards this end, we present the first large-scale empirical study of MCP
servers. Using state-of-the-art health metrics and a hybrid analysis pipeline,
combining a general-purpose static analysis tool with an MCP-specific scanner,
we evaluate 1,899 open-source MCP servers to assess their health, security, and
maintainability. Despite MCP servers demonstrating strong health metrics, we
identify eight distinct vulnerabilities - only three overlapping with
traditional software vulnerabilities. Additionally, 7.2% of servers contain
general vulnerabilities and 5.5% exhibit MCP-specific tool poisoning. Regarding
maintainability, while 66% exhibit code smells, 14.4% contain nine bug patterns
overlapping with traditional open-source software projects. These findings
highlight the need for MCP-specific vulnerability detection techniques while
reaffirming the value of traditional analysis and refactoring practices.

---

## 2. Mind the Metrics: Patterns for Telemetry-Aware In-IDE AI Application Development using the Model Context Protocol (MCP)

**Authors:** Vincent Koc, Jacques Verre, Douglas Blank, Abigail Morgan

**Published:** 2025-05-14

**Categories:** 

**URL:** [http://arxiv.org/pdf/2506.11019v1](http://arxiv.org/pdf/2506.11019v1)

**Abstract:**
AI development environments are evolving into observability first platforms
that integrate real time telemetry, prompt traces, and evaluation feedback into
the developer workflow. This paper introduces telemetry aware integrated
development environments (IDEs) enabled by the Model Context Protocol (MCP), a
system that connects IDEs with prompt metrics, trace logs, and versioned
control for real time refinement. We present design patterns for local prompt
iteration, CI based optimization, and autonomous agents that adapt behavior
using telemetry. Rather than focusing on a single algorithm, we describe an
architecture that supports integration with frameworks like DSPy, PromptWizard,
and Prompts as Programs. We demonstrate this through Opik, an open source MCP
server for LLM telemetry, and position our approach within the emerging LLMOps
ecosystem. This work lays a foundation for future research on prompt
optimization, IDE agent tooling, and empirical benchmarking in telemetry rich
AI development workflows.

---

## 3. Enhancing Clinical Decision Support and EHR Insights through LLMs and the Model Context Protocol: An Open-Source MCP-FHIR Framework

**Authors:** Abul Ehtesham, Aditi Singh, Saket Kumar

**Published:** 2025-06-13

**Categories:** 

**URL:** [http://arxiv.org/pdf/2506.13800v1](http://arxiv.org/pdf/2506.13800v1)

**Abstract:**
Enhancing clinical decision support (CDS), reducing documentation burdens,
and improving patient health literacy remain persistent challenges in digital
health. This paper presents an open-source, agent-based framework that
integrates Large Language Models (LLMs) with HL7 FHIR data via the Model
Context Protocol (MCP) for dynamic extraction and reasoning over electronic
health records (EHRs). Built on the established MCP-FHIR implementation, the
framework enables declarative access to diverse FHIR resources through
JSON-based configurations, supporting real-time summarization, interpretation,
and personalized communication across multiple user personas, including
clinicians, caregivers, and patients. To ensure privacy and reproducibility,
the framework is evaluated using synthetic EHR data from the SMART Health IT
sandbox (https://r4.smarthealthit.org/), which conforms to the FHIR R4
standard. Unlike traditional approaches that rely on hardcoded retrieval and
static workflows, the proposed method delivers scalable, explainable, and
interoperable AI-powered EHR applications. The agentic architecture further
supports multiple FHIR formats, laying a robust foundation for advancing
personalized digital health solutions.

---

## 4. Survey of LLM Agent Communication with MCP: A Software Design Pattern Centric Review

**Authors:** Anjana Sarkar, Soumyendu Sarkar

**Published:** 2025-05-26

**Categories:** 

**URL:** [http://arxiv.org/pdf/2506.05364v1](http://arxiv.org/pdf/2506.05364v1)

**Abstract:**
This survey investigates how classical software design patterns can enhance
the reliability and scalability of communication in Large Language Model
(LLM)-driven agentic AI systems, focusing particularly on the Model Context
Protocol (MCP). It examines the foundational architectures of LLM-based agents
and their evolution from isolated operation to sophisticated, multi-agent
collaboration, addressing key communication hurdles that arise in this
transition. The study revisits well-established patterns, including Mediator,
Observer, Publish-Subscribe, and Broker, and analyzes their relevance in
structuring agent interactions within MCP-compliant frameworks. To clarify
these dynamics, the article provides conceptual schematics and formal models
that map out communication pathways and optimize data flow. It further explores
architectural variations suited to different degrees of agent autonomy and
system complexity. Real-world applications in domains such as real-time
financial processing and investment banking are discussed, illustrating how
these patterns and MCP can meet specific operational demands. The article
concludes by outlining open challenges, potential security risks, and promising
directions for advancing robust, interoperable, and scalable multi-agent LLM
ecosystems.

---

## 5. Beyond the Protocol: Unveiling Attack Vectors in the Model Context Protocol Ecosystem

**Authors:** Hao Song, Yiming Shen, Wenxuan Luo, Leixin Guo, Ting Chen, Jiashui Wang, Beibei Li, Xiaosong Zhang, Jiachi Chen

**Published:** 2025-05-31

**Categories:** 

**URL:** [http://arxiv.org/pdf/2506.02040v2](http://arxiv.org/pdf/2506.02040v2)

**Abstract:**
The Model Context Protocol (MCP) is an emerging standard designed to enable
seamless interaction between Large Language Model (LLM) applications and
external tools or resources. Within a short period, thousands of MCP services
have already been developed and deployed. However, the client-server
integration architecture inherent in MCP may expand the attack surface against
LLM Agent systems, introducing new vulnerabilities that allow attackers to
exploit by designing malicious MCP servers. In this paper, we present the first
systematic study of attack vectors targeting the MCP ecosystem. Our analysis
identifies four categories of attacks, i.e., Tool Poisoning Attacks, Puppet
Attacks, Rug Pull Attacks, and Exploitation via Malicious External Resources.
To evaluate the feasibility of these attacks, we conduct experiments following
the typical steps of launching an attack through malicious MCP servers:\nupload-download-attack. Specifically, we first construct malicious MCP servers
and successfully upload them to three widely used MCP aggregation platforms.\nThe results indicate that current audit mechanisms are insufficient to identify
and prevent the proposed attack methods. Next, through a user study and
interview with 20 participants, we demonstrate that users struggle to identify
malicious MCP servers and often unknowingly install them from aggregator
platforms. Finally, we demonstrate that these attacks can trigger harmful
behaviors within the user's local environment-such as accessing private files
or controlling devices to transfer digital assets-by deploying a
proof-of-concept (PoC) framework against five leading LLMs. Additionally, based
on interview results, we discuss four key challenges faced by the current
security ecosystem surrounding MCP servers. These findings underscore the
urgent need for robust security mechanisms to defend against malicious MCP
servers.

---

## 6. Beyond Formal Semantics for Capabilities and Skills: Model Context Protocol in Manufacturing

**Authors:** Luis Miguel Vieira da Silva, Aljosha Köcher, Felix Gehlhoff

**Published:** 2025-06-12

**Categories:** 

**URL:** [http://arxiv.org/pdf/2506.11180v1](http://arxiv.org/pdf/2506.11180v1)

**Abstract:**
Explicit modeling of capabilities and skills -- whether based on ontologies,
Asset Administration Shells, or other technologies -- requires considerable
manual effort and often results in representations that are not easily
accessible to Large Language Models (LLMs). In this work-in-progress paper, we
present an alternative approach based on the recently introduced Model Context
Protocol (MCP). MCP allows systems to expose functionality through a
standardized interface that is directly consumable by LLM-based agents. We
conduct a prototypical evaluation on a laboratory-scale manufacturing system,
where resource functions are made available via MCP. A general-purpose LLM is
then tasked with planning and executing a multi-step process, including
constraint handling and the invocation of resource functions via MCP. The
results indicate that such an approach can enable flexible industrial
automation without relying on explicit semantic models. This work lays the
basis for further exploration of external tool integration in LLM-driven
production systems.

---

## 7. Context-aware Code Summary Generation

**Authors:** Chia-Yi Su, Aakash Bansal, Yu Huang, Toby Jia-Jun Li, Collin McMillan

**Published:** 2024-08-16

**Categories:** 

**URL:** [http://arxiv.org/pdf/2408.09006v1](http://arxiv.org/pdf/2408.09006v1)

**Abstract:**
Code summary generation is the task of writing natural language descriptions
of a section of source code. Recent advances in Large Language Models (LLMs)\nand other AI-based technologies have helped make automatic code summarization a
reality. However, the summaries these approaches write tend to focus on a
narrow area of code. The results are summaries that explain what that function
does internally, but lack a description of why the function exists or its
purpose in the broader context of the program. In this paper, we present an
approach for including this context in recent LLM-based code summarization. The
input to our approach is a Java method and that project in which that method
exists. The output is a succinct English description of why the method exists
in the project. The core of our approach is a 350m parameter language model we
train, which can be run locally to ensure privacy. We train the model in two
steps. First we distill knowledge about code summarization from a large model,\nthen we fine-tune the model using data from a study of human programmer who
were asked to write code summaries. We find that our approach outperforms GPT-4
on this task.

---

## 8. Context-Enhanced Vulnerability Detection Based on Large Language Model

**Authors:** Yixin Yang, Bowen Xu, Xiang Gao, Hailong Sun

**Published:** 2025-04-23

**Categories:** 

**URL:** [http://arxiv.org/pdf/2504.16877v1](http://arxiv.org/pdf/2504.16877v1)

**Abstract:**
Vulnerability detection is a critical aspect of software security. Accurate
detection is essential to prevent potential security breaches and protect
software systems from malicious attacks. Recently, vulnerability detection
methods leveraging deep learning and large language models (LLMs) have garnered
increasing attention. However, existing approaches often focus on analyzing
individual files or functions, which limits their ability to gather sufficient
contextual information. Analyzing entire repositories to gather context
introduces significant noise and computational overhead. To address these
challenges, we propose a context-enhanced vulnerability detection approach that
combines program analysis with LLMs. Specifically, we use program analysis to
extract contextual information at various levels of abstraction, thereby
filtering out irrelevant noise. The abstracted context along with source code
are provided to LLM for vulnerability detection. We investigate how different
levels of contextual granularity improve LLM-based vulnerability detection
performance. Our goal is to strike a balance between providing sufficient
detail to accurately capture vulnerabilities and minimizing unnecessary
complexity that could hinder model performance. Based on an extensive study
using GPT-4, DeepSeek, and CodeLLaMA with various prompting strategies, our key
findings includes: (1) incorporating abstracted context significantly enhances
vulnerability detection effectiveness; (2) different models benefit from
distinct levels of abstraction depending on their code understanding
capabilities; and (3) capturing program behavior through program analysis for
general LLM-based code analysis tasks can be a direction that requires further
attention.

---

## 9. LONGCODEU: Benchmarking Long-Context Language Models on Long Code Understanding

**Authors:** Jia Li, Xuyuan Guo, Lei Li, Kechi Zhang, Ge Li, Jia Li, Zhengwei Tao, Fang Liu, Chongyang Tao, Yuqi Zhu, Zhi Jin

**Published:** 2025-03-06

**Categories:** 

**URL:** [http://arxiv.org/pdf/2503.04359v1](http://arxiv.org/pdf/2503.04359v1)

**Abstract:**
Current advanced long-context language models offer great potential for
real-world software engineering applications. However, progress in this
critical domain remains hampered by a fundamental limitation: the absence of a
rigorous evaluation framework for long code understanding. To gap this
obstacle, we propose a long code understanding benchmark LONGCODEU from four
aspects (8 tasks) to evaluate LCLMs' long code understanding ability required
for practical applications, including code unit perception, intra-code unit
understanding, inter-code unit relation understanding, and long code
documentation understanding. We evaluate 9 popular LCLMs on LONGCODEU (i.e., 6
general models and 3 code models). Our experimental results reveal key
limitations in current LCLMs' capabilities for long code understanding.\nParticularly, the performance of LCLMs drops dramatically when the long code\nlength is greater than 32K, falling far short of their claimed 128K-1M context
windows. In the four aspects, inter-code unit relation understanding is the
most challenging for LCLMs. Our study provides valuable insights for optimizing
LCLMs and driving advancements in software engineering.

---

## 10. Requirements Satisfiability with In-Context Learning

**Authors:** Sarah Santos, Travis Breaux, Thomas Norton, Sara Haghighi, Sepideh Ghanavati

**Published:** 2024-04-19

**Categories:** 

**URL:** [http://arxiv.org/pdf/2404.12576v1](http://arxiv.org/pdf/2404.12576v1)

**Abstract:**
Language models that can learn a task at inference time, called in-context
learning (ICL), show increasing promise in natural language inference tasks. In
ICL, a model user constructs a prompt to describe a task with a natural
language instruction and zero or more examples, called demonstrations. The
prompt is then input to the language model to generate a completion. In this
paper, we apply ICL to the design and evaluation of satisfaction arguments,
which describe how a requirement is satisfied by a system specification and
associated domain knowledge. The approach builds on three prompt design
patterns, including augmented generation, prompt tuning, and chain-of-thought
prompting, and is evaluated on a privacy problem to check whether a mobile app
scenario and associated design description satisfies eight consent requirements
from the EU General Data Protection Regulation (GDPR). The overall results show
that GPT-4 can be used to verify requirements satisfaction with 96.7% accuracy
and dissatisfaction with 93.2% accuracy. Inverting the requirement improves
verification of dissatisfaction to 97.2%. Chain-of-thought prompting improves
overall GPT-3.5 performance by 9.0% accuracy. We discuss the trade-offs among
templates, models and prompt strategies and provide a detailed analysis of the
generated specifications to inform how the approach can be applied in practice.

---

