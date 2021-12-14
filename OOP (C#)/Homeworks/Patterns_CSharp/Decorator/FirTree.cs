using System;
using System.Collections.Generic;
using System.Text;

namespace Decorator
{
    class FirTree : IComponent
    {

        public void Execute() 
        {
            Console.WriteLine("That's a fir tree right here!");
            Console.WriteLine(@"
          .     .  .      +     .      .          .
     .       .      .     #       .           .
        .      .         ###            .      .      .
      .      .   '#:. .:##'##:. .:#'  .      .
          .      . '####'###'####'  .
       .     '#:.    .:#'###'#:.    .:#'  .        .       .
  .             '#########'#########'        .        .
        .    '#:.  '####'###'####'  .:#'   .       .
     .     .  '#######''##'##''#######'                  .
                .'##'#####'#####'##'           .      .
    .   '#:. ...  .:##'###'###'##:.  ... .:#'     .
      .     '#######'##'#####'##'#######'      .     .
    .    .     '#####''#######''#####'.      .
            .     '      000      '.     .
       .         .   .   000.        .       .
  ......................O000O.................................
");
        }
    }
}
