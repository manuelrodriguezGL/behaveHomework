from behave import given, when, then

from acceptance.page_model import Blender
from acceptance.page_model.Blender import Blender


@given('I put "{thing}" in a blender')
def step_given_put_thing_into_blender(context, thing):
    context.blender = Blender()
    context.blender.add(thing)


@when('I switch the blender on')
def step_when_switch_blender_on(context):
    context.blender.switch_on()


@then('it should transform into "{other_thing}"')
def step_then_should_transform_into(context, other_thing):
    assert context.blender.result == other_thing
