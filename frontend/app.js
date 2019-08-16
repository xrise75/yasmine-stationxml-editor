/*
 * yasmine  (Yet Another Station Metadata INformation Editor), a tool to
 * create and edit station metadata informations in FDSN stationXML format,
 * is a common development of IRIS and RESIF.
 * Development and addition of new features is shared and agreed between
 * IRIS and RESIF.
 *
 * Version 1.0 of the software was funded by SAGE, a major facility fully
 * funded by the National Science Foundation (EAR-1261681-SAGE),
 * development done by ISTI and led by IRIS Data Services.
 * Version 2.0 of the software was funded by CNRS and development led by
 * RESIF.
 *
 * This program is free software; you can redistribute it
 * and/or modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 3 of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be
 * useful, but WITHOUT ANY WARRANTY; without even the implied warranty
 * of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU Lesser General Public License (GNU-LGPL) for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this software. If not, see
 * <https://www.gnu.org/licenses/>
 *
 * This file is generated and updated by Sencha Cmd. You can edit this file as
 * needed for your application, but these edits will have to be merged by
 * Sencha Cmd when upgrading.
 */
Ext.application({
    name: 'yasmine',

    extend: 'yasmine.Application',

    requires: [
        'yasmine.view.main.Main'
    ],

    // The name of the initial view to create. With the classic toolkit this class
    // will gain a "viewport" plugin if it does not extend Ext.Viewport. With the
    // modern toolkit, the main view will be added to the Viewport.
    //
    mainView: 'yasmine.view.main.Main'

    //-------------------------------------------------------------------------
    // Most customizations should be made to yasmine.Application. If you need to
    // customize this file, doing so below this section reduces the likelihood
    // of merge conflicts when upgrading to new versions of Sencha Cmd.
    //-------------------------------------------------------------------------
});
