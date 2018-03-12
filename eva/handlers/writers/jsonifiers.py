from handlers.readers.information_map import USER_INFORMATION_MAP


class Jsonify(object):
    @classmethod
    def user_history_data(cls, user_information_list):
        json_response = {}

        course_name_value = user_information_list[USER_INFORMATION_MAP["nome_curso"]]
        workload_value = user_information_list[USER_INFORMATION_MAP["carga_horaria"]]
        teaching_format_value = user_information_list[USER_INFORMATION_MAP["formato"]]
        enrollment_status_value = user_information_list[USER_INFORMATION_MAP["sit_matricula"]]
        class_status_value = user_information_list[USER_INFORMATION_MAP["sit_turma"]]

        json_response["course_name"] = course_name_value
        json_response["workload"] = workload_value
        json_response["teaching_format"] = teaching_format_value
        json_response["enrollment"] = enrollment_status_value
        json_response["class_status"] = class_status_value

        return json_response
