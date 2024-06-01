from behave import given, when, then
import subprocess
import sys

@given('the characteristics "{char1}" and "{char2}"')
def step_given_characteristics(context, char1, char2):
    context.characteristics = [char1, char2]

@given('the abstract blocks "{block}"')
def step_given_abstract_blocks(context, block):
    context.abstract_blocks = [block]

@when('I run the script with mode "{mode}"')
def step_when_run_script_with_mode(context, mode):
    context.mode = mode
    result = subprocess.run([sys.executable, 'input_domain_modeling.py',
                             '--characteristics'] + context.characteristics +
                            ['--abstract_blocks'] + context.abstract_blocks +
                            ['--mode', context.mode], capture_output=True, text=True)
    context.output = result.stdout.strip()

@then('the output should be')
def step_then_output_should_be(context):
    expected_output = context.text.strip()
    
    # Normalize whitespace and newlines
    def normalize(output):
        return "\n".join([line.strip() for line in output.strip().split("\n")])
    
    expected_output_normalized = normalize(expected_output)
    actual_output_normalized = normalize(context.output)
    
    assert actual_output_normalized == expected_output_normalized, (
        f"Expected:\n{expected_output_normalized}\n\nGot:\n{actual_output_normalized}"
    )
