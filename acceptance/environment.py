def before_all(context):
    print_custom("Into before all hook")


def after_all(context):
    print_custom("Into after all hook")


def before_step(context, step):
    step_start_status = step.status.name


def after_step(context, step):
    step_finish_status = step.status.name


def before_scenario(context, scenario):
    scenario_start_status = scenario.status


def after_scenario(context, scenario):
    scenario_finish_status = scenario.status


def before_feature(context, feature):
    feature_before = feature.duration


def after_feature(context, feature):
    feature_after = feature.duration


def before_tag(context, tag):
    if tag == "smoke":
        print_custom("This is part of a smoke testing")


def before_rule(context, rule):
    print_custom(rule)


def after_tag(context, tag):
    if tag == "clean_something":
        print_custom("We are going to clean something right now")


def print_custom(text):
    print("\n\n******************************************************************************")
    print(text)
    print("******************************************************************************\n\n")
