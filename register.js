const {REST} = require('@discordjs/rest');
const {Routes} = require('discord-api-types/v9');
const commands = [
  {
    name: 'album',
    description: 'Get the album of the day',
  },
];

const rest = new REST({version: '9'}).setToken(process.env.TOKEN);

(async () => {
  try {
    console.log('Started refreshing application (/) commands.');

    await rest.put(Routes.applicationGuildCommands(process.env.APP_ID, process.env.GUILD_ID), {
      body: commands,
    });

    console.log('Successfully reloaded application (/) commands.');
  } catch (error) {
    console.error(error);
  }
})();