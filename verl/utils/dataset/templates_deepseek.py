
templates = {
    "abel": """
{{- bos_token}}
{{- 'Please reason step by step, and put your final answer within \\\\boxed{}.'}}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor -%}
{{- '<｜Assistant｜>' + "Let's think step by step.\n"}}
""",
    "simplerl": """
{{- bos_token}}
{{- 'You are a helpful assistant.'}}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content'] + '\n' + 'Please reason step by step, and put your final answer within \\\\boxed{}.' }}
{%- endif %}
{%- endfor -%}
{{- '<｜Assistant｜>\n'}}
""",
    "qwen-math": """
{{- bos_token}}
{{- 'Please reason step by step, and put your final answer within \\\\boxed{}.'}}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor -%}
{{- '<｜Assistant｜>\n'}}
""",
    "r1-distilled": """
{{- bos_token}}
{{- 'Please reason step by step, and put your final answer within \\\\boxed{}.'}}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor -%}
{{- '<｜Assistant｜><think>\n'}}
""",
    "open-r1": """
{{- bos_token}}
{{- 'You are a helpful AI Assistant that provides well-reasoned and detailed responses. You first think about the reasoning process as an internal monologue and then provide the user with the answer. Respond in the following format: <think>\n...\n</think>\n<answer>\n...\n</answer>\nInside the <answer>...</answer> block, the final answer must be enclosed in \\\\boxed{}.'}}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor -%}
{{- '<｜Assistant｜>'}}
""",
    "open-r1-teacher": """
{{- bos_token}}
{{- 'You are a helpful AI Assistant that provides well-reasoned and detailed responses. You first think about the reasoning process as an internal monologue and then provide the user with the answer. Respond in the following format: <think>\n...\n</think>\n<answer>\n...\n</answer>\nInside the <answer>...</answer> block, the final answer must be enclosed in \\\\boxed{}.'}}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor -%}
{{- '<｜Assistant｜><think>\n'}}
""",
    "deepseek-r1": """
{{- bos_token}}
{{- 'A conversation between User and Assistant. The User asks a question, and the Assistant solves it. The Assistant first thinks about the reasoning process in the mind and then provides the User with the answer. The reasoning process is enclosed within <think> </think> and answer is enclosed within <answer> </answer> tags, respectively, i.e., <think> reasoning process here </think> <answer> answer here </answer>. Inside the <answer>...</answer> block, the final answer must be enclosed in \\\\boxed{}.'}}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor -%}
{{- '<｜Assistant｜>'}}
""",
    "deepseek-r1-teacher": """
{{- bos_token}}
{{- 'A conversation between User and Assistant. The User asks a question, and the Assistant solves it. The Assistant first thinks about the reasoning process in the mind and then provides the User with the answer. The reasoning process is enclosed within <think> </think> and answer is enclosed within <answer> </answer> tags, respectively, i.e., <think> reasoning process here </think> <answer> answer here </answer>. Inside the <answer>...</answer> block, the final answer must be enclosed in \\\\boxed{}.'}}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor -%}
{{- '<｜Assistant｜><think>'}}
""",
    "formal": """
{{- bos_token}}
{{-'You are an intelligent assistant who helps with user questions. Provide a rigorous, step-by-step derivation of the solution. The final answer must be clearly indicated within \\\\boxed{}.'}}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor -%}
{{- '<｜Assistant｜>\n'}}
""",
    "lm_eval_prompt1": """
{{- bos_token}}
{{- 'Solve the following math challenge. Explain your approach step-by-step\nThe answer should end with: The final answer is: \\\\boxed{answer}\nwhere [answer] is just the final number or expression that solves the problem'}}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor -%}
{{- "<｜Assistant｜>Let's think step by step"}}
""",
    "lm_eval_prompt4": """
{{- bos_token}}
{{- 'Analyze and solve the math task.'}}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content'] + '\n' + 'End the answer with:\nThe final answer is: \\\\boxed{answer} where [answer] is just the final number or expression that solves the problem.'}}
{%- endif %}
{%- endfor -%}
{{- '<｜Assistant｜>\n'}}
""",
    "lm_eval_prompt8": """
{{- bos_token}}
{{- 'Solve the following math problem\nShow each step of your solution\nPut the final answer within \\\\boxed{}'}}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor -%}
{{- "<｜Assistant｜>Let's think step by step"}}
""",
#     "reflective_prompt": """
# {{- bos_token}}
# {{- "You are a helpful assistant that solves math problems. Always write out your reasoning to produce a solution, then check whether the solution is correct, fix it if it is wrong, and finally give the final answer. Respond in exactly the following format: <solution>\nreasoning and solution\n</solution>\n<check>\nLet's verify step by step ...\n</check>\nPut your final answer within \\\\boxed{}."}}
# {%- for message in messages %}
# {%- if message['role'] == 'user' %}
# {{- '<｜User｜>' + message['content']}}
# {%- endif %}
# {%- endfor -%}
# {{- '<｜Assistant｜>'}}
# """,
#     "reflective_prompt-teacher": """
# {{- bos_token}}
# {{- "You are a helpful assistant that solves math problems. Always write out your reasoning to produce a solution, then check whether the solution is correct, fix it if it is wrong, and finally give the final answer. Respond in exactly the following format: <solution>\nreasoning and solution\n</solution>\n<check>\nLet's verify step by step ...\n</check>\nPut your final answer within \\\\boxed{}."}}
# {%- for message in messages %}
# {%- if message['role'] == 'user' %}
# {{- '<｜User｜>' + message['content']}}
# {%- endif %}
# {%- endfor -%}
# {{- '<｜Assistant｜><solution>\n'}}   
# """,

# ---------- STEP-BY-STEP (CORE SIGNAL) ----------

"stepwise_v1": """
{{- bos_token}}
{{- 'Solve step by step and ensure the final answer is enclosed in \\\\boxed{}.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>Let's solve this step by step.\n" }}
""",


"stepwise_v2": """
{{- bos_token}}
{{- 'Carefully derive the solution step by step. Final answer must be in \\\\boxed{}.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>\n" }}
""",



"stepwise_v3": """
{{- bos_token}}
{{- 'Provide a detailed reasoning process. Conclude with \\\\boxed{}.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>Start reasoning:\n" }}
""",

"stepwise_v4": """
{{- bos_token}}
{{- 'Break the problem into steps and solve sequentially. Final answer in \\\\boxed{}.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>\n" }}
""",


"strict_format_v1": """
{{- bos_token}}
{{- 'Follow strict reasoning. Do not skip steps. Final answer must be in \\\\boxed{}.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>\n" }}
""",


"strict_format_v2": """
{{- bos_token}}
{{- 'Explain clearly and end precisely with \\\\boxed{}.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>Proceed carefully:\n" }}
""",


"strict_format_v3": """
{{- bos_token}}
{{- 'Ensure logical correctness at every step. Final answer strictly inside \\\\boxed{}.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>\n" }}
""",

"lm_eval_prompt9": """
{{- bos_token}}
{{- 'Solve the problem and show reasoning. End with:\nWe conclude that the answer is: \\\\boxed{answer}' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>\n" }}
""",

"lm_eval_prompt10": """
{{- bos_token}}
{{- 'Work through the math problem step by step. Finish with:\nTherefore, the final answer is \\\\boxed{answer}' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>Let's think carefully.\n" }}
""",


"lm_eval_prompt11": """
{{- bos_token}}
{{- 'Provide reasoning and ensure the answer ends with:\nBased on the analysis, the answer is: \\\\boxed{answer}' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>\n" }}
""",


"lm_eval_prompt12": """
{{- bos_token}}
{{- 'Explain your reasoning step by step, and conclude with a final statement of the form:\nFrom the steps above, the answer is \\\\boxed{answer}' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>\n" }}
""",

"concise_v1": """
{{- bos_token}}
{{- 'Provide concise but sufficient reasoning. Final answer must be in \\\\boxed{}.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>\n" }}
""",

"concise_v2": """
{{- bos_token}}
{{- 'Solve briefly but include key steps. End with \\\\boxed{}.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>\n" }}
""",


"r1_strict_v7_teacher": """
{{- bos_token}}
{{- 'Solve the following problem.\nFormat:\n<think>\n...\n</think>\n<answer>\n\\\\boxed{}\n</answer>\nEnsure correctness and proper formatting.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜><think>\n" }}
""",


"r1_strict_v7": """
{{- bos_token}}
{{- 'Solve the following problem.\nFormat:\n<think>\n...\n</think>\n<answer>\n\\\\boxed{}\n</answer>\nEnsure correctness and proper formatting.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>" }}
""",


"r1_strict_v3_teacher": """
{{- bos_token}}
{{- 'Solve the problem carefully and ensure correctness.\nUse this exact format:\n<think>...</think><answer>...</answer>\nThe answer must be enclosed in \\\\boxed{}.\nAll tags must be properly closed.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜><think>" }}
""",


"r1_strict_v3": """
{{- bos_token}}
{{- 'Solve the problem carefully and ensure correctness.\nUse this exact format:\n<think>...</think><answer>...</answer>\nThe answer must be enclosed in \\\\boxed{}.\nAll tags must be properly closed.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>" }}
""",

"r1_strict_v8_teacher": """
{{- bos_token}}
{{- 'You are given a problem to solve.\nUse this structure exactly:\n<think>\n...\n</think>\n<answer>\n...\n</answer>\nFinal answer must be enclosed in \\\\boxed{}.\nDo not skip steps.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜><think>\n" }}
""",

"r1_strict_v8_teacher": """
{{- bos_token}}
{{- 'You are given a problem to solve.\nUse this structure exactly:\n<think>\n...\n</think>\n<answer>\n...\n</answer>\nFinal answer must be enclosed in \\\\boxed{}.\nDo not skip steps.' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>" }}
""",

"think_only_v5_teacher": """
{{- bos_token}}
{{- 'Your task is to solve the given problem correctly.\nAll reasoning must be inside <think></think>.\nThe final answer must be enclosed in \\\\boxed{}.\nEnsure correctness before answering.\n' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜><think>" }}
""",


"think_only_v5": """
{{- bos_token}}
{{- 'Your task is to solve the given problem correctly.\nAll reasoning must be inside <think></think>.\nThe final answer must be enclosed in \\\\boxed{}.\nEnsure correctness before answering.\n' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>" }}
""",


"think_only_v9_teacher": """
{{- bos_token}}
{{- 'Solve the problem step by step.\nOrganize your reasoning clearly inside <think></think>.\nThe final answer must be in \\\\boxed{}.\n' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜><think>" }}
""",

"think_only_v9": """
{{- bos_token}}
{{- 'Solve the problem step by step.\nOrganize your reasoning clearly inside <think></think>.\nThe final answer must be in \\\\boxed{}.\n' }}
{%- for message in messages %}
{%- if message['role'] == 'user' %}
{{- '<｜User｜>' + message['content']}}
{%- endif %}
{%- endfor %}
{{- "<｜Assistant｜>" }}
""",



}

from jinja2 import Template

if __name__ == "__main__":
    for name, tpl in templates.items():
        try:
            Template(tpl)
        except Exception as e:
            print("BROKEN:", name)
            raise
