#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2018
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains an object that represents a Telegram ReplyKeyboardMarkup."""

from telegram import ReplyMarkup


class ReplyKeyboardMarkup(ReplyMarkup):
    """This object represents a custom keyboard with reply options.
       이 객체는 답변 옵션에 대한 커스텀 키보드를 표현합니다.
    Attributes:
        keyboard (List[List[:class:`telegram.KeyboardButton` | :obj:`str`]]): Array of button rows.
        버튼 row 배열
        resize_keyboard (:obj:`bool`): Optional. Requests clients to resize the keyboard.
        선택형이며, 클라이언트에게 키보드 사이즈를 조정하도록 request
        one_time_keyboard (:obj:`bool`): Optional. Requests clients to hide the keyboard as soon as
            it's been used.
        선택형, 클라이언트에게 키보드 사용 후 바로 감추도록 request
        selective (:obj:`bool`): Optional. Show the keyboard to specific users only.
        선택형, 특정 사용자에게만 키보드가 보이도록 함.

    Example:
        A user requests to change the bot's language, bot replies to the request with a keyboard
        to select the new language. Other users in the group don't see the keyboard.
        사용자가 봇의 language를 변경하도록 요청하면 봇은 새로운 language를 선택하기 위해 키보드로 request에 대한 답변을 한다.
        해당 그룹의 다른 사용자들은 이 키보드를 볼 수 없다.

    Args:
        keyboard (List[List[:obj:`str` | :class:`telegram.KeyboardButton`]]): Array of button rows,
                each represented by an Array of :class:`telegram.KeyboardButton` objects.
                버튼 row 배열, 각 항목은 :class:`telegram.KeyboardButton 객체의 배열에 따라 표현이 된다.
        resize_keyboard (:obj:`bool`, optional): Requests clients to resize the keyboard vertically
            for optimal fit (e.g., make the keyboard smaller if there are just two rows of
            buttons). Defaults to false, in which case the custom keyboard is always of the same
            height as the app's standard keyboard. Defaults to ``False``
        one_time_keyboard (:obj:`bool`, optional): Requests clients to hide the keyboard as soon as
            it's been used. The keyboard will still be available, but clients will automatically
            display the usual letter-keyboard in the chat - the user can press a special button in
            the input field to see the custom keyboard again. Defaults to ``False``.
        selective (:obj:`bool`, optional): Use this parameter if you want to show the keyboard to
            specific users only. Targets:

            1) users that are @mentioned in the text of the Message object
            2) if the bot's message is a reply (has reply_to_message_id), sender of the original
               message.

            Defaults to ``False``.

        **kwargs (:obj:`dict`): Arbitrary keyword arguments.

    """

    def __init__(self,
                 keyboard,
                 resize_keyboard=False,
                 one_time_keyboard=False,
                 selective=False,
                 **kwargs):
        # Required
        self.keyboard = keyboard
        # Optionals
        self.resize_keyboard = bool(resize_keyboard)
        self.one_time_keyboard = bool(one_time_keyboard)
        self.selective = bool(selective)

    def to_dict(self):
        data = super(ReplyKeyboardMarkup, self).to_dict()

        data['keyboard'] = []
        for row in self.keyboard:
            r = []
            for button in row:
                if hasattr(button, 'to_dict'):
                    r.append(button.to_dict())  # telegram.KeyboardButton
                else:
                    r.append(button)  # str
            data['keyboard'].append(r)
        return data
