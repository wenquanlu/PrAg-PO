import re


# should be very limited words after last boxed
def abel_format_reward(completion):
    return 1.0

def simplerl_format_reward(completion):
    return 1.0

def qwen_math_format_reward(completion):
    return 1.0

def stepwise_v1_reward(completion):
    return 1.0

def stepwise_v2_reward(completion):
    return 1.0

def stepwise_v3_reward(completion):
    return 1.0

def stepwise_v4_reward(completion):
    return 1.0

def strict_format_v1_reward(completion):
    return 1.0

def strict_format_v2_reward(completion):
    return 1.0

def strict_format_v3_reward(completion):
    return 1.0





def open_r1_format_reward(completion):
    """Reward function that checks if the reasoning process is enclosed within <think> and </think> tags, while the final answer is enclosed within <answer> and </answer> tags."""
    count = 0.0
    if completion.count("<think>\n") == 1:
        count += 0.25
    if completion.count("\n</think>\n") == 1:
        count += 0.25
    if completion.count("\n<answer>\n") == 1:
        count += 0.25
    if completion.count("\n</answer>") == 1:
        count += 0.25
    
    return count

def open_r1_teacher_format_reward(completion):
    count = 0.0
    if completion.count("\n</think>\n") == 1:
        count += 1/3
    if completion.count("\n<answer>\n") == 1:
        count += 1/3
    if completion.count("\n</answer>") == 1:
        count += 1/3
    return count

def deepseek_r1_format_reward(completion):
    count = 0.0
    if completion.count("<think>") == 1:
        count += 0.25
    if completion.count("</think>") == 1:
        count += 0.25
    if completion.count("<answer>") == 1:
        count += 0.25
    if completion.count("</answer>") == 1:
        count += 0.25
    return count

def deepseek_r1_teacher_format_reward(completion):
    count = 0.0
    if completion.count("</think>") == 1:
        count += 1/3
    if completion.count("<answer>") == 1:
        count += 1/3
    if completion.count("</answer>") == 1:
        count += 1/3
    return count


def r1_strict_v7_teacher_format_reward(completion):
    return open_r1_teacher_format_reward(completion)

def r1_strict_v7_format_reward(completion):
    return open_r1_format_reward(completion)

def r1_strict_v3_teacher_format_reward(completion):
    return deepseek_r1_teacher_format_reward(completion)

def r1_strict_v3_format_reward(completion):
    return deepseek_r1_format_reward(completion)

def r1_strict_v8_teacher_format_reward(completion):
    return deepseek_r1_teacher_format_reward(completion)

def r1_strict_v8_format_reward(completion):
    return deepseek_r1_format_reward(completion)

def r1_distilled_reward(completion):
    count = 0.0
    if completion.count("</think>") == 1:
        count += 1
    return count

def think_only_v5_teacher_format_reward(completion):
    count = 0.0
    if completion.count("</think>") == 1:
        count += 1
    return count

def think_only_v5_format_reward(completion):
    count = 0.0
    if completion.count("<think>") == 1:
        count += 0.5
    if completion.count("</think>") == 1:
        count += 0.5
    return count

def think_only_v9_teacher_format_reward(completion):
    return think_only_v5_teacher_format_reward(completion)

def think_only_v9_format_reward(completion):
    return think_only_v5_format_reward(completion)


def open_r1_format_reward_old(completion):
    """Reward function that checks if the reasoning process is enclosed within <think> and </think> tags, while the final answer is enclosed within <answer> and </answer> tags."""
    pattern = r"^<think>\n.*?\n</think>\n<answer>\n.*?\n</answer>$"
    matches = re.match(pattern, completion, re.DOTALL | re.MULTILINE) 
    return 1.0 if matches else 0.0


def deepseek_r1_format_reward_old(completion):
    pattern = r"^<think>.*?</think> <answer>.*?</answer>$"
    matches = re.match(pattern, completion, re.DOTALL | re.MULTILINE) 
    return 1.0 if matches else 0.0


def formal_format_reward(completion):
    return 1.0

# must be ending with The final answer is: \\boxed{answer} or The final answer is: \\boxed{answer}\n or The final answer is: \\boxed{answer}.\n or The final answer is: \\boxed{answer}.
def lm_eval_prompt1_format_reward(completion):
    key = "The final answer is:"
    format_score = 1.0 if completion.count(key) == 1 else 0.0
    return format_score

# Not used
def lm_eval_prompt2_format_reward(completion):
    if completion.count("## Step 1:") != 1:
        return 0.0
    if completion.count("## Step 2:") != 1:
        return 0.0
    if completion.count("The final answer is:") != 1:
        return 0.0
    return 1.0

# must be ending with The final answer is: \\boxed{answer} or The final answer is: \\boxed{answer}\n or The final answer is: \\boxed{answer}.\n or The final answer is: \\boxed{answer}.
def lm_eval_prompt4_format_reward(completion):
    key = "The final answer is:"
    format_score = 1.0 if completion.count(key) == 1 else 0.0
    return format_score

def lm_eval_prompt9_format_reward(completion):
    key = "We conclude that the answer is:"
    format_score = 1.0 if completion.count(key) == 1 else 0.0
    return format_score

def lm_eval_prompt10_format_reward(completion):
    key = "Therefore, the final answer is"
    format_score = 1.0 if completion.count(key) == 1 else 0.0
    return format_score

def lm_eval_prompt11_format_reward(completion):
    key = "Based on the analysis, the answer is:"
    format_score = 1.0 if completion.count(key) == 1 else 0.0
    return format_score

def lm_eval_prompt12_format_reward(completion):
    key = "From the steps above, the answer is"
    format_score = 1.0 if completion.count(key) == 1 else 0.0
    return format_score

def concise_v1_reward(completion):
    return 1.0

def concise_v2_reward(completion):
    return 1.0


def lm_eval_prompt8_format_reward(completion):
    return 1.0

def check_verify_block_enough_long(completion):
    start_key = "\n<check>\nLet's verify step by step"
    end_key = "\n</check>"
    start = completion.find(start_key)
    start += len(start_key)
    end = completion.find(end_key, start)
    if end == -1:
        return False
    if len(completion[start:end].strip()) > 50:
        return True
    else:
        return False

def reflective_prompt_format_reward(completion):
    count = 0.0
    if completion.count("<solution>\n") == 1:
        count += 0.25
    if completion.count("\n</solution>\n") == 1:
        count += 0.25
    if completion.count("\n<check>\nLet's verify step by step") == 1:
        count += 0.25
        if completion.count("\n</check>") == 1 and completion.strip().endswith("\n</check>"):
            count += 0.25
            # if thing in the check is empty, or monotonic, return 0
            if not check_verify_block_enough_long(completion):
                return 0.0
    else:
        if completion.count("\n</check>") == 1 and completion.strip().endswith("\n</check>"):
            count += 0.25
    return count

def reflective_prompt_teacher_format_reward(completion):
    count = 0.0
    if completion.count("\n</solution>\n") == 1:
        count += 1/3
    if completion.count("\n<check>\nLet's verify step by step") == 1:
        count += 1/3
        if completion.count("\n</check>") == 1 and completion.strip().endswith("\n</check>"):
            count += 1/3
            # if thing in the check is empty, or monotonic, return 0
            if not check_verify_block_enough_long(completion):
                return 0.0
    else:
        if completion.count("\n</check>") == 1 and completion.strip().endswith("\n</check>"):
            count += 1/3
    return count


FORMAT_REWARDS = {
    "abel": abel_format_reward,
    "simplerl": simplerl_format_reward,
    "qwen-math": qwen_math_format_reward,
    "open-r1": open_r1_format_reward,
    "open-r1-teacher": open_r1_teacher_format_reward,
    "deepseek-r1": deepseek_r1_format_reward,
    "deepseek-r1-teacher": deepseek_r1_teacher_format_reward,
    "formal": formal_format_reward,
    "lm_eval_prompt1": lm_eval_prompt1_format_reward,
    "lm_eval_prompt4": lm_eval_prompt4_format_reward,
    "lm_eval_prompt8": lm_eval_prompt8_format_reward,
    "reflective_prompt": reflective_prompt_format_reward,
    "reflective_prompt-teacher": reflective_prompt_teacher_format_reward,
    "stepwise_v1": stepwise_v1_reward,
    "stepwise_v2": stepwise_v2_reward,
    "stepwise_v3": stepwise_v3_reward,
    "stepwise_v4": stepwise_v4_reward,
    "strict_format_v1": strict_format_v1_reward,
    "strict_format_v2": strict_format_v2_reward,
    "strict_format_v3": strict_format_v3_reward,
    "lm_eval_prompt9": lm_eval_prompt9_format_reward,
    "lm_eval_prompt10": lm_eval_prompt10_format_reward,
    "lm_eval_prompt11": lm_eval_prompt11_format_reward,
    "lm_eval_prompt12": lm_eval_prompt12_format_reward,
    "concise_v1": concise_v1_reward,
    "concise_v2": concise_v2_reward,
    "r1_strict_v7_teacher": r1_strict_v7_teacher_format_reward,
    "r1_strict_v7": r1_strict_v7_format_reward,
    "r1_strict_v3_teacher": r1_strict_v3_teacher_format_reward,
    "r1_strict_v3": r1_strict_v3_format_reward,
    "r1_strict_v8_teacher": r1_strict_v8_teacher_format_reward,
    "r1_strict_v8": r1_strict_v8_format_reward,
    "think_only_v5_teacher": think_only_v5_teacher_format_reward,
    "think_only_v5": think_only_v5_format_reward,
    "think_only_v9_teacher": think_only_v9_teacher_format_reward,
    "think_only_v9": think_only_v9_format_reward,
    "r1-distilled": r1_distilled_reward,
}

def get_format_reward(format_name, completion):
    if format_name not in FORMAT_REWARDS:
        raise ValueError(f"Unknown format reward: {format_name}")
    return FORMAT_REWARDS[format_name](completion)
