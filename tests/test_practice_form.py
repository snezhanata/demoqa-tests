from selene import have, command, be
from selene.support.shared import browser
import tests.conftest
from demoqa_tests.utils import path, common
from demoqa_tests.utils import table
from tests.test_data.users import user


def test_submit_student_registration_form():
    """
    This test checks the submission of the "Student Registration Form"
    """

    # GIVEN
    tests.conftest.given_opened_practice_form()

    # WHEN
    browser.should(have.title('ToolsQA'))
    browser.element('#firstName').type(user.name)
    browser.element('#lastName').type(user.last_name)
    browser.element('#userEmail').type(user.email)
    browser.all('[for^=gender-radio]').by(
        have.exact_text(user.gender.value)
    ).first.click()
    ''' 
    OR
    browser.element('#gender-radio-2').double_click() - это неверный селектор, был бы верным, если бы завернули в переменную вот так:
    gender_female = browser.element('#gender-radio-2')
    gender_female.double_click()

    OR 
    browser.element('#genterWrapper').all('custom-radio').element_by(have.exact_text(user.gender.value)).click()

    OR
    browser.element('[id^=gender-radio][value=Male]').perform(command.js.click)  # селектор Баранцева
    Баранцев сказал бы, что этот селектор лучше, потому что он семантически лучше объясняет о чем речь

    OR
    Но если вдруг нет вэлью, то нужно написать вот так:
    female_gender_radio = browser.element('#gender-radio-2')
    female_gender_radio.click()

    OR
    browser.all('[id^=gender-radio]').element_by(have.value('Male')).element('..').click()  # селектор от Яши

    OR
    browser.all('[id^=gender-radio]').by(have.value('Male')).first.element('..').click()  # это обновленный селектор от Яши,
    первый элемент из коллекции

    OR
    browser.element('[id^=gender-radio][value=Male]').element('./following-sibling::*').click() # xpath если бы у лейбла не было for

    OR
    browser.element('[id^=gender-radio][value=Male]').element('..').click() # и label, и input живут в div custom-radio, поэтому сиблинг заменяем на перента
    '''
    browser.element('#userNumber').type(user.mobile_number)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(user.birth_month)
    browser.element('.react-datepicker__year-select').send_keys(user.birth_year)
    browser.element(
        f'.react-datepicker__day--0{user.birth_day}'
        f':not(.react-datepicker__day--outside-month)'
    ).click()
    '''
    OR
    browser.element('#dateOfBirthInput').perform(command.js.set_value('30 August,2000'))

    OR
    browser.element('#dateOfBirthInput').with_(set_value_by_js=True).set_value('30 August,2000')

    OR
    browser.element('.react-datepicker__month-select').element(f'[value="{user.birth_month}"]').click()
    browser.element('.react-datepicker__year-select').element(f'[value="{user.birth_year}"]').click()
    browser.element(f'.react-datepicker__day--0{user.birth_day}').click()

    OR
    browser.element('.react-datepicker__year-select').element('[value="2000"]').click()
    browser.element('.react-datepicker__month-select').element('[value="7"]').click()
    browser.element('.react-datepicker__day--008').click()

    OR
    # we can set value in Calendar also just using: 
    browser.element('#dateOfBirthInput').type('01 Sep 2001')

    OR
    # сэмулировать с помощью комбинации клавиш, но код не будет кроссплатформенным
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('01 Sep 2001').press_enter()
    '''
    for subject in user.subjects:
        browser.element('#subjectsInput').type(subject.value).press_enter()
    '''
    OR
    browser.element('#subjectsInput').type('Maths').press_enter()

    OR
    browser.element('#subjectsInput').type('Computer Science')
    browser.all('.subjects-auto-complete__option').element_by(have.text('Computer Science')).perform(command.js.click)

    OR
    select.autocomplete('#subjectsInput', from_='Com', to='Computer Science')

    OR Spoiler(Class)
    TagsInput('#subjectsInput').type('Com').select('Computer Science')
    TagsInput('#subjectsInput').type('Com').autocomplete
    '''
    for hobby in user.hobbies:
        browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element(
            '..'
        ).click()

    '''
    OR
    for hobby in user.hobbies:
        browser.all('[for^=hobbies]').by(have.exact_text(hobby.value)).first.click()

    OR
    for hobby in user.hobbies:
        browser.element(f'//label[contains(.,"{hobby.value}")]').click()

    OR
    for hobby in user.hobbies:
        browser.element(by.text(hobby.value)).click()

    OR
    browser.element('[for="hobbies-checkbox-1"]').click()

    OR
    browser.element('#hobbiesWrapper').all('.custom-checkbox').element_by(have.exact_text('Music')).click()

    OR
    Если будут не value, а текстовые Sports,Reading, Music, а значения вот здесь:
    class Hobby(Enum):
        Sports = 'Sports'
        Reading = 'Reading'
        Music = 'Music'
    То можно будет переписать вот так:
    for hobby in user.hobbies:
        browser.all('[for^=hobbies]').by(have.exact_text(hobby.value)).first.click()

    OR 
    music_hobby = browser.element('[for="hobbies-checkbox-1"]')
    music_hobby.click()

    '''
    browser.element('#uploadPicture').send_keys(path.to_resource(user.picture_file))
    '''
    OR
    picture_file = os.path.join(Path(resources.__file__).parent.absolute(), user.picture_file)
    browser.element('#uploadPicture').send_keys(picture_file)

    OR
    def resource_abs_path(relative_path):
        return os.path.join(Path(resources.__file__).parent.absolute(), relative_path)
    browser.element('#uploadPicture').send_keys(resource_abs_path(user.picture_file))

    OR
    browser.element('#uploadPicture').send_keys(path_to_resource('resources/pic.jpg'))

    OR
    browser.element('#uploadPicture').perform(path.upload_resource('pic.jpg'))
    '''
    browser.element('#currentAddress').type(user.current_address)
    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(user.state)
    ).first.click()  # react-select-3-option-2
    '''
    # OR
    # browser.element('#state').element('[id$=-input]').type(user.state).press_tab()
    # 
    # OR
    # browser.element('#state').perform(command.js.click)
    # browser.element('#react-select-3-input').type(user.state).press_enter()
    # '''
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=-option-]').by(
        have.exact_text(user.city)
    ).first.click()
    '''
    OR
    browser.element('#city').element('[id$=-input]').type(user.city).press_tab()

    OR    
    browser.element('#city').perform(command.js.click)
    browser.element('#react-select-4-input').type(user.city).press_enter()
    '''
    browser.element('#submit').perform(command.js.click)
    '''
    OR
    browser.element('#submit').with_(click_by_js=True).click()

    OR
    browser.element('#submit').press_enter()

    OR
    submit = browser.element('#submit').with_(click_by_js=True)
    submit.click()
    submit.click()
    submit.click()
    '''

    # THEN

    browser.element('#example-modal-sizes-title-lg').should(be.visible)
    '''
    OR
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    '''

    table.should_have_view(
        ('Student Name', f'{user.name} {user.last_name}'),
        ('Student Email', user.email),
        ('Gender', user.gender.value),
        ('Mobile', user.mobile_number),
        ('Date of Birth', f'{user.birth_day} {user.birth_month},{user.birth_year}'),
        ('Subjects', ', '.join([subject.value for subject in user.subjects])),
        # ('Subjects', f'{user.subjects[0].value}, {user.subjects[1].value}'),
        # ('Subjects', ', '.join(map(lambda s: s.value, user.subjects))),
        ('Hobbies', ', '.join([hobby.name for hobby in user.hobbies])),
        # ('Hobbies', f'{user.hobbies[0].value}'),
        # ('Subjects', ', '.join(map(lambda s: s.value, user.hobbies))),
        ('Picture', user.picture_file),
        ('Address', user.current_address),
        ('State and City', f'{user.state} {user.city}'),
    )


'''
OR
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    rows.all('td').should(
        have.exact_texts(
            'Student Name',
            f'{user.name} {user.last_name}',
            'Student Email',
            user.email,
            'Gender',
            user.gender.value,
            'Mobile',
            user.mobile_number,
            'Date of Birth',
            f'{user.birth_day} {user.birth_month},{user.birth_year}',
            'Subjects',
            ', '.join([subject.value for subject in user.subjects]),
            'Hobbies',
            ', '.join([hobby.value for hobby in user.hobbies]),
            'Picture',
            user.picture_file,
            'Address',
            user.current_address,
            'State and City',
            f'{user.state} {user.city}',
        )
    )

OR (указать even и проверять только второй столбец значений)
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    rows.all('td').even.should(have.exact_texts(
        f'{user.name} {user.last_name}',
        user.email,
        user.gender.value,
        user.user_number,
        f'{user.birth_day} {user.birth_month},{user.birth_year}',
        f'{user.subjects[0].value}, {user.subjects[1].value}',
        ', '.join([hobby.value for hobby in user.hobbies]),
        user.picture_file,
        user.current_address,
        f'{user.state} {user.city}'
    )

OR
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    rows.all('td').should(
        have.exact_texts(
            *flatten([
                ('Student Name', f'{yuri.name} {yuri.last_name}'),
                ('Student Email', yuri.email),
                ('Gender', yuri.gender.value),
                ('Mobile', yuri.user_number),
                ('Date of Birth', f'{yuri.birth_day} {yuri.birth_month},{yuri.birth_year}'),
                ('Subjects', ', '.join([subject.value for subject in yuri.subjects])),
                ('Hobbies', ', '.join([hobby.name for hobby in yuri.hobbies])),
                ('Picture', yuri.picture_file),
                ('Address', yuri.current_address),
                ('State and City', f'{yuri.state} {yuri.city}'),
                ]
            )
        )
    )

    OR
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    rows.all('td').element_by(have.exact_text('Student Name')).element('./following-sibling::td')
    .should(have.exact_text(f'{user.name} {user.last_name}'))

    OR
    dialog = browser.element('.modal-content')
    rows = dialog.all('tbody tr')
    rows.all('td').by(have.exact_text('Student Name')).first.element('./following-sibling::td')
    .should(have.exact_text(f'{user.name} {user.last_name}')) # first == [0]

    OR
    browser.element_by(have.text('Student Name')).all('td')[1].should(have.exact_text(f'{user.name} {user.last_name}'))

    OR
    browser.element('.modal-dialog').all('table tr')[1].all('td')[1].should(have.exact_text(f'{user.name} {user.last_name}')) # лучше указать, что именно окошко появляется modal-dialog

    OR
    browser.all('table tr')[5].all('td')[1].should(have.exact_texts('Date of Birth', f'{user.birth_day} {user.birth_month},{user.birth_year}')) # здесь проверяем значения двух столбцов

    OR
    def cells_of_row_should_have_texts(index, *texts):  # можно создать метод
        browser.element('.modal-dialog').all('table tr')[index].all('td')[1].should(have.exact_texts(*texts))
    table.cells_of_row_should_have_texts(1, 'Student Name', f'{user.name} {user.last_name}')

    OR
    browser.element('.table-responsive').all('tr')[1].element('td')[1].should(have.exact_text(f'{user.name} {user.last_name}'))

'''
