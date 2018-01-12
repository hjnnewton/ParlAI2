from parlai.core.teachers import DialogTeacher
from .build import build
from parlai.core.teachers import FbDialogTeacher
import json

import copy
import os


def _path(opt):
    # Build the data if it doesn't exist.
    build(opt)

    questions_path = os.path.join(opt['datapath'], 'chitchat', "train", 'questions.txt')
    answers_path = os.path.join(opt['datapath'], 'chitchat', "train", 'answers.txt')
    path = questions_path + ':' + answers_path
    return path
    # return os.path.join(opt['datapath'], 'chitchat', '{type}.txt'.format(type=dt))


# class DefaultTeacher(DialogTeacher):
#     def __init__(self, opt, shared=None):
#         opt = copy.deepcopy(opt)
#         opt['datafile'] = _path(opt, '')
#         opt['task'] = 'smartvoice'
#         super().__init__(opt, shared)



class SVTeacher(DialogTeacher):
    def __init__(self, opt, shared=None):
        task = opt.get('task', 'smartvoice')
        self.datatype = opt['datatype']
        self.path = _path(opt)
        opt['datafile'] = self.path
        self.id = 'Chitchat'
        self.text = 'Question'
        super().__init__(opt, shared)

    def setup_data(self, path):
        print('loading question from: ' + path)
        a_path = path.split(':')[1]
        q_path = path.split(':')[0]
        episode_done = True
        with open(q_path) as q_file:
            with open(a_path) as a_file:
                self.labels = a_file.readlines()
                self.questions = q_file.readlines()
        for i in range(len(self.labels)):
            question = self.questions[i].strip("\n")
            label = [self.labels[i].strip("\n")]

            yield (question, label,None , None), episode_done
        #yield (None, self.answers, self.questions, ), new_episode




# def setup_data(path):
#     print('loading: ' + path)
#     if path is None:
#         return "", ""
#     with open(path) as data_file:
#         lines = data_file.readlines()
#         for line in lines:
#             json_line = json.load(line)
#             yield json_line["text1"], json_line["text2"]



class DefaultTeacher(SVTeacher):
    pass

